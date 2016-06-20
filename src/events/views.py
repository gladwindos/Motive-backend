from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import EventForm
from .models import Event

@login_required(login_url='/login/')
def event_create(request):

	form = EventForm(request.POST or None, request.FILES or None)

	form_button = "Create event"

	if form.is_valid() and request.user.is_authenticated():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Event created")
		return HttpResponseRedirect(instance.get_absolute_url())
	if form.errors:
		messages.error(request, "Error creating event")

	context = {
		"form": form,
		"form_button": form_button,

	}
	return render(request, "event_form.html", context)


def event_feed(request):

	title = "Feed"

	queryset_list = Event.objects.all()

	if request.path == reverse("my-events", kwargs={}):
		title = "My Events"

		queryset_list = Event.objects.all().filter(user=request.user)

	query = request.GET.get('q')

	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query) |
				Q(user__username__icontains=query)
				).distinct()


	paginator = Paginator(queryset_list, 3)

	page_request_var = 'page'

	page = request.GET.get(page_request_var)
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"title": title,
		"page_request_var": page_request_var,

	}
	return render(request, "event_feed.html", context)



def event_detail(request, id=None):

	instance = get_object_or_404(Event, id=id)

	context = {
		"title": "detail",
		"instance": instance,

	}
	return render(request, "event_detail.html", context)	

@login_required(login_url='/login/')
def event_update(request, id=None):

	instance = get_object_or_404(Event, id=id)

	form = EventForm(request.POST or None, request.FILES or None, instance=instance)

	form_button = "Update event"

	if form.is_valid() and request.user.is_authenticated():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Event updated")
		return HttpResponseRedirect(instance.get_absolute_url())
	if form.errors:
		messages.error(request, "Error updating event")

	context = {
		"form": form,
		"instance": instance,
		"form_button": form_button,

	}
	return render(request, "event_form.html", context)

@login_required(login_url='/login/')
def event_delete(request, id=None):

	try:
		obj = Event.objects.get(id=id)
	except:
		raise Http404

	if obj.user != request.user and not request.user.is_superuser:
		response = HttpResponse("You do not have permission to do this!")
		response.status_code = 403
		return response

	obj.delete()
	messages.success(request, "This event has been deleted.")
	return redirect("events:feed")



