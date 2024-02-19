from django.views import View
from django.shortcuts import render
from .forms import FeedbackForm

class HomePageView(View):
    template_name = 'lab5/index.html'

    def get(self, request):
        form = FeedbackForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = FeedbackForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            my_message = form.cleaned_data['my_message']
            review_area = form.cleaned_data['review_area']
            context['my_message'] = my_message

            if 'srvc' in review_area:
                context['service_evaluated'] = True
            else:
                context['service_evaluated'] = False

            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, context)
        
class ThankYouPageView(View):
    template_name = 'lab5/thanks.html'

    def get(self, request):
        
        my_name = "austin"
        return render(request, self.template_name,{'my_name':my_name})
