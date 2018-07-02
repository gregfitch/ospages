"""Test of admin console."""

from tests.markers import expected_failure, nondestructive, test_case, tutor


@expected_failure
@nondestructive
@test_case('')
@tutor
def test_navbar_elements_present(tutor_base_url, selenium, admin):
    """Test admin console navbar elements present."""
    # GIVEN: logged in as admin

    # WHEN: Go to admin console

    # THEN: User is able to see the navbar with the following elements:
    # "Tutor Admin Console", "Course Organization", "Content",
    # "Legal", "Stats", "Users", "Job", "Payments", "Research Data",
    # "Salesforce", "System Setting".


@expected_failure
@nondestructive
@test_case('')
@tutor
def test_view_student(tutor_base_url, selenium, admin):
    """Test to view students in a course."""
    # GIVEN: logged in as admin
    # AND: At the Course Organization Page

    # WHEN: In the drop down click on ""Courses""
    # AND: Click the ""List Students"" button next to one of the courses

    # THEN: A list of students in the course is displayed
