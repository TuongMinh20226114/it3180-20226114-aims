def search_by_title(items, keyword):
    """Tìm kiếm các đĩa DVD có tiêu đề chứa từ khóa."""
    return [dvd for dvd in items if keyword in dvd.title]
