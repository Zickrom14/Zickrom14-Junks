from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Message
from .forms import MessageForm
from django.http import JsonResponse
from .models import DraftMessage

# Home page view
def home(request):
    return render(request, 'home.html')

# Write message view
from django.http import JsonResponse

def write_message(request, message_id=None):
    message = get_object_or_404(Message, id=message_id) if message_id else None

    if request.method == 'POST':
        form = MessageForm(request.POST, instance=message)
        
        if 'send' in request.POST and form.is_valid():  # Check if Send button was clicked
            message_instance = form.save(commit=False)
            message_instance.status = 'sent'
            message_instance.save()
            return redirect('sent_messages')
        
        elif 'save_draft' in request.POST:  # Save as draft
            if form.is_valid():
                draft_instance = form.save(commit=False)
                draft_instance.status = 'draft'
                draft_instance.save()
                return JsonResponse({'success': True})
    
    else:
        form = MessageForm(instance=message)

    return render(request, 'write_message.html', {'form': form, 'message_id': message_id})

# Sent messages view
def sent_messages(request):
    messages = Message.objects.filter(status='sent')
    return render(request, 'sent_messages.html', {'messages': messages})

# Draft messages view
def draft_messages(request):
    drafts = Message.objects.filter(status='draft')
    return render(request, 'draft_messages.html', {'drafts': drafts})

# Delete message view
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message.delete()
    return redirect('sent_messages')

# Delete draft
def delete_draft(request, draft_id):
    draft = get_object_or_404(Message, id=draft_id)
    draft.delete()
    return redirect('draft_messages')

# About us
def about(request):
    return render(request, 'about.html')