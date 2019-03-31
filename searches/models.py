from django.db import models

class Complaint(models.Model):
    INITIALIZED = 'INITIALIZED'
    WAITING_FOR_APPROVAL = 'WAIT_FOR_APP'
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'
    UNKNOWN = 'UNKNOWN'

    STATUSES = (
        (INITIALIZED, 'Initializd'),
        (WAITING_FOR_APPROVAL, 'Waiting For Approval'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (UNKNOWN, 'Unknown')
    )

    name = models.CharField(max_length=255, unique=True)
    doi = models.DateField('date of incident')
    poi = models.CharField(max_length=255, verbose_name='place of incident')
    fir = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUSES, default=INITIALIZED)
    status_msg = models.TextField(null=True)
    submitter = models.ForeignKey('users.User', on_delete=models.DO_NOTHING, related_name='complaints')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Searchee(models.Model):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    NON_BINARY = 'NON_BINARY'
    GENDERS = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NON_BINARY, 'Non Binary')
    )

    SKIN_TONE_LIGHT = 'ST_LIGHT'
    SKIN_TONE_MEDIUM = 'ST_MEDIUM'
    SKIN_TONE_DARK = 'ST_DARK'
    SKIN_TONES = (
        (SKIN_TONE_LIGHT, 'Light'),
        (SKIN_TONE_MEDIUM, 'Medium'),
        (SKIN_TONE_DARK, 'Dark'),
    )

    full_name = models.CharField(max_length=255)
    dob = models.DateField(verbose_name='date of birth')
    sex = models.CharField(max_length=20,choices=GENDERS,null=True)
    height_cm = models.DecimalField(verbose_name='height in cm',max_digits=3,decimal_places=2,null=True)
    weight_kg = models.IntegerField(verbose_name='weight in kg', null=True)
    skin_tone = models.CharField(max_length=20,choices=SKIN_TONES,null=True)
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, related_name='searchees')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class SearcheeSample(models.Model):
    searchee = models.ForeignKey(Searchee, on_delete=models.CASCADE, related_name='samples')
    image_url = models.TextField()
    userability = models.IntegerField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Search(models.Model):
    INITIALIZED = 'INITIALIZED'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'
    ERROR = 'ERROR'
    STATUSES = (
        (INITIALIZED, 'Initialized'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
        (ERROR, 'Error')
    )
    
    searchee = models.ForeignKey(Searchee, on_delete=models.CASCADE, related_name='searches')    
    name = models.CharField(max_length=255)
    video = models.TextField(verbose_name='video source url')
    location = models.CharField(max_length=255, null=True, verbose_name='name of the location')
    lat = models.CharField(max_length=255, null=True)
    long = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=20, choices=STATUSES, default=INITIALIZED)
    progress = models.IntegerField(default=0, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if (self.pk):
            pass
        super(Search, self).save(*args, **kwargs)
 
    def __str__(self):
        return self.name


class SearchResult(models.Model):
    search = models.ForeignKey(Search, on_delete=models.CASCADE, related_name='results')
    timestamp_sec = models.IntegerField(verbose_name='timestamp where appeared')
    x1 = models.IntegerField(default=0, verbose_name='x1 coordinate')
    y1 = models.IntegerField(default=0, verbose_name='y1 coordinate')
    x2 = models.IntegerField(default=0, verbose_name='x2 coordinate')
    y2 = models.IntegerField(default=0, verbose_name='y2 coordinate')
    image = models.TextField(null=True)
    confidence = models.IntegerField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)