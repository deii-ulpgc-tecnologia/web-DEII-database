import os
from django.core.exceptions import ValidationError

# Limits in bytes per general content type
LIMITS_BY_CATEGORY = {
    'image': 5 * 1024 * 1024,        # 5 MB
    'video': 50 * 1024 * 1024,       # 50 MB
    'audio': 20 * 1024 * 1024,       # 20 MB
    'application': 1 * 1024 * 1024, # 10 MB (e.g. PDFs)
    'text': 1 * 1024 * 1024,         # 1 MB
}
DEFAULT_LIMIT = 5 * 1024 * 1024

# Minimal extension -> category map for fallback when content_type missing
EXT_CATEGORY_MAP = {
    'pdf': 'application',
    'txt': 'text',
    'csv': 'text',
    'jpg': 'image',
    'jpeg': 'image',
    'png': 'image',
    'gif': 'image',
    'webp': 'image',
    'mp4': 'video',
    'mov': 'video',
    'mp3': 'audio',
    'wav': 'audio',
}


def file_size_by_category_validator(f):
    """
    Validator that enforces max file size depending on the general content type
    (image/, video/, audio/, application/, text/). Falls back to extension mapping
    or DEFAULT_LIMIT when content_type is not available.
    """
    size = getattr(f, 'size', 0)
    content_type = getattr(f, 'content_type', None)

    max_size = None
    if isinstance(content_type, str) and '/' in content_type:
        category = content_type.split('/', 1)[0].lower()
        max_size = LIMITS_BY_CATEGORY.get(category)

    if max_size is None:
        # fallback by extension (safe if content_type not present)
        name = getattr(f, 'name', '') or ''
        ext = name.rsplit('.', 1)[-1].lower() if '.' in name else ''
        mapped_category = EXT_CATEGORY_MAP.get(ext)
        if mapped_category:
            max_size = LIMITS_BY_CATEGORY.get(mapped_category, DEFAULT_LIMIT)
        else:
            max_size = DEFAULT_LIMIT

    if size > max_size:
        # give a helpful message; use bytes or MB as you prefer
        mb = max_size / (1024 * 1024)
        raise ValidationError(
            f"File '{getattr(f, 'name', '')}' exceeds the allowed size "
            f"for its type (max {mb:.1f} MB)."
        )

# Allowed extensions derived from the extension->category map
ALLOWED_EXTENSIONS = EXT_CATEGORY_MAP.keys()

def extension_whitelist_validator(f):
    """
    Reject files whose extension is not in ALLOWED_EXTENSIONS.
    Raises django.core.exceptions.ValidationError on failure.
    """
    name = getattr(f, 'name', '') or ''
    # reject if no extension
    if '.' not in name:
        raise ValidationError(f"File '{name}' has no extension or an unsupported extension.")
    ext = name.rsplit('.', 1)[-1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValidationError(f"Extension '.{ext}' is not allowed.")
    # success: do nothing