from django.shortcuts import render,redirect
from django.contrib import messages
# import MySQLdb
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import ProfileUpdateForm
from allauth.account.decorators import verified_email_required

#@verified_email_required
#@login_required
def adminconsoleView(request):
    # conn = MySQLdb.connect(host="67.43.13.32", user="tcklk_webClient", password="71542140Lk#",
    #                        database="tcklk_tckEstoredb")
    # try:
    #     cursor = conn.cursor()
    #     cursor.execute("select sales from Sales")
    #     salesData = cursor.fetchall()
    #
    #     cursor.execute("select sales from Sales order by sales desc limit 4")
    #     dailySalesData = cursor.fetchall()
    #
    #     cursor.execute("select revenue from Sales order by revenue desc limit 4")
    #     revenueData = cursor.fetchall()
    #
    #     cursor.execute("select DATE_FORMAT(date,'%m/%d/%Y') from Sales order by sales desc limit 4")
    #     dateData = cursor.fetchall()
    #
    #     datedataArray = []
    #     salesdataArray = []
    #     revenuedataArray = []
    #     dailysales = 0
    #     for i in salesData:
    #         salesdataArray.append(i[0])
    #     for ii in revenueData:
    #         revenuedataArray.append(ii[0])
    #     for iii in dateData:
    #         noSlashes = iii[0].replace("/", "-")
    #         datedataArray.append(noSlashes)
    #     for i in dailySalesData:
    #         dailysales =+ 1
    #
    #
    #     context = {
    #         "salesdataArray": salesdataArray,
    #         "revenuedataArray": revenuedataArray,
    #         "datedataArray": datedataArray,
    #         "dailysales" : dailysales
    #     }
    #
    #
    #
    # finally:
    #     conn.close()
    return render(request, 'webFrontend/admin-console.html')


#@login_required
def profileView(request):

    return render(request, 'webFrontend/profile.html')


#@verified_email_required
#@login_required
def profileupdateView(request):
    if request.method== 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            name = profile_form.cleaned_data.get('first_name')
            profile_form.save()
            messages.success(request, f'Account details have been successfully updated for {name}.')
            return redirect('profileUrl')
    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'profile_form' : profile_form }
    return render(request, 'webFrontend/edit-profile.html', context)


#@login_required
def contactView(request):

    return render(request, 'webFrontend/contact.html')


#@login_required
def faqView(request):

    return render(request, 'webFrontend/faq.html')


#@login_required
def accountsettingsView(request):

    return render(request, 'webFrontend/account-settings.html')


#@login_required
def welcomeView(request):




    return render(request, 'webFrontend/selection-page.html')


#@verified_email_required
#@login_required
def selectshopView(request):

    return render(request, 'webFrontend/selection-page.html')