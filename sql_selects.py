def select_all_columns_and_rows():
    return cursor.execute("SELECT * FROM planets;").fetchall()

def select_name_and_color_of_all_planets():
    return cursor.execute("SELECT name, color FROM planets;").fetchall()

def select_all_planets_with_mass_greater_than_one():
    return cursor.execute("SELECT * FROM planets WHERE mass >1.00;").fetchall()

def select_name_and_mass_of_planets_with_mass_less_than_equal_to_one():
    return cursor.execute("SELECT name, mass FROM planets WHERE mass <= 1.00;").fetchall()

def select_name_and_color_of_planets_with_more_than_10_moons():
    return cursor.execute("SELECT name, color FROM planets WHERE num_of_moons > 10;").fetchall()

def select_all_planets_with_moons_and_mass_less_than_one():
    return cursor.execute("SELECT * FROM planets WHERE mass < 1.00 AND num_of_moons > 0;").fetchall()

def select_name_and_color_of_all_blue_planets():
    return cursor.execute("SELECT name, color FROM planets WHERE color == 'blue' OR color == 'light blue' OR color == 'dark blue';").fetchall()