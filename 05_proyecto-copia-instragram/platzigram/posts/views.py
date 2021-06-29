
from django.shortcuts import render

#utilities
from datetime import datetime

posts = [
    {
        'name':'Jackson Reyes',
        'user':'jreyes',
        'timestamp': datetime.now().strftime('%b %d, %Y - %H:%M'),
        'picture':'https://picsum.photos/200/200?image=1036',
    },
        {
        'name':'Jackson Reyes',
        'user':'jreyes',
        'timestamp': datetime.now().strftime('%b %d, %Y - %H:%M'),
        'picture':'https://picsum.photos/200/200?image=903',
    },
    {
        'name':'Jackson Reyes',
        'user':'jreyes',
        'timestamp': datetime.now().strftime('%b %d, %Y - %H:%M'),
        'picture':'https://picsum.photos/200/200?image=1076',
    }
]
# Create your views here.
def postList(request):
    
    return render(request,'feed.html',{'posts':posts})