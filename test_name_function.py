from name_function import get_formatted_name as gfn

def test_first_last_name ():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = gfn("Janis", "Joplin")
    assert formatted_name == "Japnis Joplin"
