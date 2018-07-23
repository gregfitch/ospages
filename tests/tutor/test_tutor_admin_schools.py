"""Test of admin console schools page."""

from tests.markers import expected_failure, nondestructive, test_case, tutor


@expected_failure
@nondestructive
@test_case('')
@tutor
def test_add_school(tutor_base_url, selenium, admin):
    """Test admin to add a school."""
    # GIVEN: logged in as admin
    # AND: At the Schools page

    # WHEN: Click the ""Add School"" button
    # AND: Fill out the required fields
    # AND: Click the ""Save"" button

    # THEN: The new school is added to schools list


@expected_failure
@nondestructive
@test_case('')
@tutor
def test_edit_school(tutor_base_url, selenium, admin):
    """Test admin to edit a school."""
    # GIVEN: logged in as admin
    # AND: At the Schools page

    # WHEN: Click the edit button next to a school
    # AND: Update one or more fields
    # AND: Click the ""Save"" button

    # THEN: The edited school is correctly updated


@expected_failure
@nondestructive
@test_case('')
@tutor
def test_delete_schoole(tutor_base_url, selenium, admin):
    """Test admin to delete a school."""
    # GIVEN: logged in as admin
    # AND: At the Schools Page

    # WHEN: Next to a school click the ""Delete"" button
    # AND: Click ""Okay""

    # THEN: The deleted school is removed from the list of schools
