from django.shortcuts import render,redirect
from  django.core.urlresolvers import reverse
from blog.models import *
from blog.forms import TopicForm,EntryForm

# Create your views here.

#首页
def index(request):
    '''学习笔记的首页'''
    return render(request,'blog/index.html',{'title':'首页'})

#主题页
def topics(request):
    '''显示所有主题'''
    topics=Topic.objects.order_by('date_added')
    context={
        'topics':topics,
        'title':'主题页'
             }
    return  render(request, 'blog/topics.html', context)

#主题详情页
def topic(request,topic_id):
    '''显示当个主题及其所有条目'''
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by('data_added')
    context={
        'entries':entries,
        'title':'主题详情页' ,
        'topic':topic
    }
    return  render(request,'blog/topic.html',context)

#主题创建页面
def new_topic(request):
    '''添加新主题'''
    if request.method!='POST':
        #未提交数据：创建一个新表单
        form=TopicForm()
    else:
        #POST提交的数据，对数据进行处理
        form=TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:topics'))

    context={
            'form':form,
            'title':'主题创建页面'
    }
    return render(request,'blog/new_topic.html',context)

#条目创建页面
def new_entry(request,topic_id):
    '''添加新条目'''
    topic=Topic.objects.get(id=topic_id)
    if request.method!='POST':
        form=EntryForm()
    else:
        form=EntryForm(request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            return redirect(reverse('blog:topic',args=[topic_id] ))
    context={
        'form':form,
        'title':'条目创建页面',
        'topic':topic
    }

    return  render(request,'blog/new_entry.html',context)

#编辑条目页面
def edit_entry(request,entry_id):
    '''编辑既有条目'''
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic

    if request.method!='POST':
        form=EntryForm(instance=entry)
    else:
        form=EntryForm(data=request.POST,instance=entry)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:topic',args=[topic.id]))

    context={
        'form':form,
        'title':'编辑条目页面',
        'topic':topic,
        'entry':entry
    }
    return  render(request,'blog/edit_entry.html',context)
