def next_available_row(worksheet):
    """
    Takes worksheet object and the next row with no content.
    """
    str_list = list(filter(None, worksheet.col_values(1)))
    return len(str_list) + 1
