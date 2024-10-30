from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Chat
from .forms import ChatForm

@login_required
def chat_list(request):
    chats = Chat.objects.filter(recipient=request.user) | Chat.objects.filter(sender=request.user)
    return render(request, 'chat/chat_list.html', {'chats': chats})

@login_required
def chat_create(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.sender = request.user
            chat.save()
            return redirect('chat_list')
    else:
        form = ChatForm()
    return render(request, 'chat/chat_form.html', {'form': form})

@login_required
def chat_delete(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    if chat.sender == request.user:
        chat.delete()
    return redirect('chat_list')
