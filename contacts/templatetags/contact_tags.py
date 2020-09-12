from django import template
from contacts.forms import ContactForm

register = template.Library()

@register.inclusion_tag("contacts/tag/contact_form.html")
def contact_form():
    return {'contact_form':ContactForm()}
