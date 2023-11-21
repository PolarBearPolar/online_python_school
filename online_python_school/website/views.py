from django.shortcuts import render
from django.http import JsonResponse
from .models import Topic
from .helpers import stdout_io

def index(request):
    all_topics = Topic.objects.order_by("topic_seq").all
    # Process post request
    if request.method == "POST":
        import json
        python_script = json.loads(request.body.decode("utf-8"))
        with stdout_io() as s:
            try:
                exec(python_script["pytonScript"])
            except Exception as err:
                print(f"Something is wrong with the code:\n{err}")
        data = dict()
        data["pytonScripOutput"] = s.getvalue()
        return JsonResponse(
            data,
            safe=False
        )
    # Process get request
    if request.method == "GET":
        topic_id = request.GET.get("topicId")
        if topic_id:
            topic = Topic.objects.get(id=topic_id)
            return render(
                request, 
                "index.html", 
                {
                    'all':all_topics,
                    'selected_topic': topic
                }
            )
        # Render empty page
        else:
            return render(
                request, 
                "index.html", 
                {
                    'all':all_topics
                }
            )

def about(request):
    all_topics = Topic.objects.order_by("topic_seq").all
    return render(
        request, 
        "about.html", 
        {
            'all':all_topics
        }
    )
