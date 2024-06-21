from typing import Any
from .forms import ReviewForm
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Review


class ReviewView(CreateView):
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"


class SingleReviewView(DetailView):
    model = Review
    template_name = "reviews/single_review.html"


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        Review.objects.get(pk=review_id)
