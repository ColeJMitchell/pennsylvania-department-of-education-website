from django.db import models

class School(models.Model):
    school_id = models.IntegerField(primary_key=True)
    district_id = models.IntegerField()
    name = models.CharField(max_length=100)
    address_city = models.CharField(max_length=100)
    address_state = models.CharField(max_length=100)
    address_street = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    zip = models.IntegerField()
    telephone = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    elementary = models.BooleanField()
    middle = models.BooleanField()
    high = models.BooleanField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

class SchoolEnrollment(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    year = models.IntegerField()
    two_or_more_races_percent = models.FloatField()
    american_indian_alaska_native_percent = models.FloatField()
    asian_percent = models.FloatField()
    black_african_american_percent = models.FloatField()
    # dropouts_female = models.IntegerField()
    # dropouts_male = models.IntegerField()
    economically_disadvantaged_percent = models.FloatField()
    english_learner_percent = models.FloatField()
    # foster_care_percent = models.FloatField()
    hispanic_percent = models.FloatField()
    homeless_percent = models.FloatField()
    # low_income_percent = models.FloatField()
    military_connected_percent = models.FloatField()
    native_hawaiian_or_pacific_islander_percent = models.FloatField()
    percent_of_gifed_students = models.FloatField()
    school_enrollment = models.IntegerField()
    special_education_percent = models.FloatField()
    title_i_school = models.BooleanField()
    white_percent = models.FloatField()

class SchoolGraduation(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    year = models.IntegerField()
    graduation_count = models.IntegerField()
    college_bound = models.IntegerField()
    two_or_four_year_college_or_university = models.IntegerField()
    total_postsecondary_bound = models.IntegerField()
    non_degree_granting_postsecondary_bound = models.IntegerField()
    specialized_associates_degree_granting_institution = models.IntegerField()

class SchoolFiscal(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    year = models.IntegerField(default=-1)
    local_non_personnel = models.FloatField(default=-1)
    local_personnel = models.FloatField(default=-1)
    state_non_personnel = models.FloatField(default=-1)
    state_personnel = models.FloatField(default=-1)
    federal_non_personnel = models.FloatField(default=-1)
    federal_personnel = models.FloatField(default=-1)

class SchoolKeystone(models.Model):
    keystone_id = models.IntegerField(primary_key=True)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    year = models.IntegerField()
    subject = models.CharField(max_length=100, default="Unknown")
    group = models.CharField(max_length=100, default="Unknown")
    numbers_scored = models.IntegerField(default=-1)
    percent_advanced = models.FloatField(default=-1)
    percent_proficient = models.FloatField(default=-1)
    percent_basic = models.FloatField(default=-1)
    percent_below_basic = models.FloatField(default=-1)

"""
class SchoolKeystone(models.Model):
    keystone_id = models.IntegerField(primary_key=True)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    year = models.IntegerField()
    subject = models.CharField(max_length=100)

class SchoolKeystoneStats(models.Model):
    keystone_id = models.ForeignKey(SchoolKeystone, on_delete=models.CASCADE)
    group = models.CharField(max_length=100)
    numbers_scored = models.IntegerField()
    percent_advanced = models.FloatField()
    percent_proficient = models.FloatField()
    percent_basic = models.FloatField()
    percent_below_basic = models.FloatField()

class SchoolPSSA(models.Model):
    pssa_id = models.IntegerField(primary_key=True)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    year = models.IntegerField()
    subject = models.CharField(max_length=100)
    grade = models.IntegerField()

class SchoolPSSAStats(models.Model):
    pssa_id = models.ForeignKey(SchoolPSSA, on_delete=models.CASCADE)
    group = models.CharField(max_length=100)
    numbers_scored = models.IntegerField()
    percent_advanced = models.FloatField()
    percent_proficient = models.FloatField()
    percent_basic = models.FloatField()
    percent_below_basic = models.FloatField()
"""
class SchoolCohort(models.Model):
    cohort_id = models.IntegerField(primary_key=True)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    year = models.IntegerField()
    num_year = models.IntegerField()

class SchoolCohortStats(models.Model):
    cohort_id = models.ForeignKey(SchoolCohort, on_delete=models.CASCADE)
    num_female = models.IntegerField()
    num_cohort = models.IntegerField()
    male_grad_rate = models.FloatField()
    female_grad_rate = models.FloatField()
    american_indian_alaska_native_grad_rate = models.FloatField()
    native_hawaiian_or_pacific_islander_grad_rate = models.FloatField()
    asian_grad_rate = models.FloatField()
    black_grad_rate = models.FloatField()
    hispanic_grad_rate = models.FloatField()
    white_grad_rate = models.FloatField()
    multi_racial_grad_rate = models.FloatField()
    special_ed_grad_rate = models.FloatField()
    english_learner_grad_rate = models.FloatField()
    economically_disadvantaged_grad_rate = models.FloatField()
    migrant_grad_rate = models.FloatField()
    foster_grad_rate = models.FloatField()
    homeless_grad_rate = models.FloatField()
    military_grad_rate = models.FloatField()

class district(models.Model):
    district_id = models.IntegerField(primary_key=True)
    district_name = models.CharField(max_length=100)
    district_address_city = models.CharField(max_length=100)
    district_address_street = models.CharField(max_length=100)
    district_zip_code = models.IntegerField()
    geographic_size_square_miles = models.FloatField()

class districtFiscal(models.Model):
    fiscal_id = models.IntegerField(primary_key=True)
    district_id = models.ForeignKey(district, on_delete=models.CASCADE)
    federal_revenue = models.FloatField()
    local_revenue = models.FloatField()
    state_revenue = models.FloatField()
    total_expenditures = models.FloatField()
    total_revenue = models.FloatField()
    year = models.IntegerField()

class districtKeystone(models.Model):
    keystone_id = models.IntegerField(primary_key=True)
    district_id = models.ForeignKey(district, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    numbers_scored = models.IntegerField()
    percent_advanced = models.FloatField()
    percent_proficient = models.FloatField()
    percent_basic = models.FloatField()
    percent_below_basic = models.FloatField()
    year = models.IntegerField()

class districtEnrollment(models.Model):
    district_id = models.ForeignKey(district, on_delete=models.CASCADE)
    year = models.IntegerField(primary_key=True)
    two_or_more_race_percent = models.FloatField()
    american_indian_alaska_native_percent = models.FloatField()
    asian_percent = models.FloatField()
    black_african_american_percent = models.FloatField()
    economically_disadvantaged_percent = models.FloatField()
    english_learner_percent = models.FloatField()
    female_percent = models.FloatField()
    foster_care_percent = models.FloatField()
    hispanic_percent = models.FloatField()
    homeless_percent = models.FloatField
    military_connected_percent = models.FloatField()
    native_hawaiian_or_pacific_islander_percent = models.FloatField()
    percent_of_gifted_students = models.FloatField()
    special_education_percent = models.FloatField()
    white_percent = models.FloatField()


class enrollment(models.Model):
    district = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    enrollmentnum = models.IntegerField()
    years = models.CharField(max_length=100)
    