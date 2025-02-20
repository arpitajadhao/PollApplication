from django.shortcuts import get_object_or_404,render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Choice, Question, Vote
from django.db.models import F
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegistrationForm






from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect("polls:index")  # Redirect to polls after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, "registration/register.html", {"form": form})



class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by("-pub_date")[:5]


class DetailView(generic.DeleteView):
    model = Question
    template_name = "polls/detail.html"
    login_url = "/accounts/login/"

    def get_queryset(self):
         """
        Excludes any questions that aren't published yet.
        """
         return Question.objects.filter(pub_date__lte = timezone.now())



class ResultsView(LoginRequiredMixin, generic.DeleteView):
    model = Question
    template_name = "polls/results.html"
    login_url = "/accounts/login/"

@login_required(login_url="/accounts/login/")
def user_vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)


    if Vote.objects.filter(user = request.user, question = question).exists():
        return render(
            request,
            "polls/detail.html",
            {
                "question":question,
                "error_message":"You have already voted for this poll!"
            },
        )
    
    try:
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't selected a choice...",
            },

        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save(update_fields = ["votes"])
        selected_choice.refresh_from_db()

        Vote.objects.create(user = request.user, question = question, choice = selected_choice)

    return HttpResponseRedirect(reverse("polls:results", args = (question.id,)))






