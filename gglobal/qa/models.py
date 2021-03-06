from django.db import models
from django.contrib.sites.models import Site
from django.conf import settings
from django.utils.text import slugify
from markdownx.models import MarkdownxField as MarkdownField

from hitcount.models import HitCountMixin
from taggit.managers import TaggableManager
from annoying.fields import AutoOneToOneField

from taggit.models import TagBase, GenericTaggedItemBase

from django.utils.translation import ugettext_lazy as _

class MyCustomTag(TagBase):
    description = models.CharField(max_length=200, blank=False, null=True)
    # ... fields here


    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class TaggedWhatever(GenericTaggedItemBase):
    # TaggedWhatever can also extend TaggedItemBase or a combination of
    # both TaggedItemBase and GenericTaggedItemBase. GenericTaggedItemBase
    # allows using the same tag for different kinds of objects, in this
    # example Food and Drink.

    # Here is where you provide your custom Tag class.
    tag = models.ForeignKey(MyCustomTag,
                            related_name="%(app_label)s_%(class)s_items", 
                            default="")


class UserQAProfile(models.Model):
    user = AutoOneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    points = models.IntegerField(default=0)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)

    def __str__(self):  # pragma: no cover
        return self.user.username


class Question(models.Model, HitCountMixin):
    slug = models.SlugField(max_length=200)
    title = models.CharField(max_length=200, blank=False)
    description = MarkdownField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    tags = TaggableManager(through=TaggedWhatever)
    reward = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default="")
    closed = models.BooleanField(default=False)
    positive_votes = models.IntegerField(default=0)
    negative_votes = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    sites = models.ManyToManyField(Site, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        self.total_points = self.positive_votes - self.negative_votes
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, default="")
    answer_text = MarkdownField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    updated = models.DateTimeField('date updated', auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default="")
    answer = models.BooleanField(default=False)
    positive_votes = models.IntegerField(default=0)
    negative_votes = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.total_points = self.positive_votes - self.negative_votes
        super(Answer, self).save(*args, **kwargs)

    def __str__(self):  # pragma: no cover
        return self.answer_text

    class Meta:
        ordering = ['-answer', '-pub_date']


class VoteParent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default="")
    value = models.BooleanField(default=True)

    class Meta:
        abstract = True


class AnswerVote(VoteParent):
    answer = models.ForeignKey(Answer, default="")

    class Meta:
        unique_together = (('user', 'answer'),)


class QuestionVote(VoteParent):
    question = models.ForeignKey(Question, default="")

    class Meta:
        unique_together = (('user', 'question'),)


class BaseComment(models.Model):
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default="")

    class Meta:
        abstract = True

    def __str__(self):  # pragma: no cover
        return self.comment_text


class AnswerComment(BaseComment):
    comment_text = MarkdownField()
    answer = models.ForeignKey(Answer, default="")


class QuestionComment(BaseComment):
    comment_text = models.CharField(max_length=250)
    question = models.ForeignKey(Question, default="")
