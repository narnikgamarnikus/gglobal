
from __future__ import absolute_import
from gglobal.service.models import Service, Trouble
from gglobal.cms.models import ServicePage, TroublePage, Service as ServiceSnippet, Trouble as TroubleSnippet, CityPage, BasePage
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

@receiver(post_save, sender=Service)
def create_service_page(sender, instance, created, **kwargs):
	citypages = CityPage.objects.all()
	basepage = BasePage.objects.first()
	if created and instance.accepted:
			for city in citypages:
				service_snippet = ServiceSnippet.objects.first()
				service_page = ServicePage(service=instance)
				service_page.snippet.add(service_snippet)
				city.add_child(inctance=service_page)
				basepage.add_child(inctance=service_page)
				service_page.save()

	elif not created and instance.accepted:
		for city in citypages:
			service_snippet = ServiceSnippet.objects.first()
			service_page = ServicePage(service=instance)
			service_page.snippet.add(service_snippet)
			city.add_child(inctance=service_page)
			basepage.add_child(inctance=service_page)
			print(basepage)
			service_page.save()


	
'''
@receiver(post_save, sender=Trouble)
def create_trouble_page(sender, instance, created, **kwargs):	
	citypages = CityPage.objects.all()
	if created and instance.accepted:
		for city in citypages:
			trouble_snippet = TroubleSnippet.objects.create(trouble=instance)
			trouble_page = TroublePage(
				trouble=trouble_snippet, 
				title='{}'.format(instance.name), 
				slug='{}'.format(instance.slug)
				)
			city.add_child(instance=trouble_page)
'''