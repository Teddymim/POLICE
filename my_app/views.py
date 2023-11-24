from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from my_app.forms import CriminalForm
from my_app.forms import CrimeForm
from my_app.forms import CasualityForm
from my_app.forms import WitnessForm
from my_app.forms import OffenceForm

from my_app.models import Criminal
from my_app.models import Crime
from my_app.models import Casuality
from my_app.models import Witness
from my_app.models import Offence

from django.shortcuts import get_object_or_404
from django.contrib import messages

#create your views here.

@login_required
def index_view(request):
        print("here")
        return render(request, 'index.html')

@login_required
def criminal_view(request):
        return render(request, 'criminal.html')

@login_required
def offence_view(request):
        return render(request, 'offence.html')


@login_required
def add_criminal_view(request):
        message = ''
        if request.method =="POST":
                criminal_form=CriminalForm(request.POST, request.FILES)

                if criminal_form.is_valid():
                        criminal_form.save()
                        messages.success(request, "Criminal Added Successfully") 
        else:
                criminal_form =CriminalForm()
        criminals = Criminal.objects.all()
                
        context ={
                'form': criminal_form,
                'msg': message,
                'criminals': criminals
        }
        
        return render(request, "add_criminal.html", context)

@login_required
def add_crime_view(request):
        message = ''
        if request.method =="POST":
                crime_form=CrimeForm(request.POST)

                if crime_form.is_valid():
                        crime_form.save()
                        messages.success(request, "Crime Added Successfully") 
                       
        else:
                crime_form =CrimeForm()
        crimes = Crime.objects.all()
                
        context ={
                'form': crime_form,
                'msg': message,
                'crimes': crimes
        }
        return render(request, "add_crime.html", context)

@login_required
def add_casuality_view(request):
        message = ''
        if request.method =="POST":
                casuality_form=CasualityForm(request.POST)
                
                if casuality_form.is_valid():
                        casuality_form.save()
                        messages.success(request, "Casuality Added Successfully") 
        else:
                casuality_form = CasualityForm()
        casualities = Casuality.objects.all()
               
        context={
                'form': casuality_form,
                'msg': message,
                'casualities': casualities
                
        }
        return render(request, "add_casuality.html", context)

@login_required
def add_witness_view(request):
        message = ''
        if request.method =="POST":
                witness_form = WitnessForm(request.POST)
                
                if witness_form.is_valid():
                        witness_form.save()
                        messages.success(request, "Witness Added Successfully") 
        
        witness_form = WitnessForm()
        witnesses = Witness.objects.all()
                
        context={
                'form': witness_form,
                'msg': message,
                'witnesses': witnesses
                
        }
        return render(request, "add_witness.html", context)

@login_required
def add_offence_view(request):
        message = ''
        if request.method =="POST":
                offence_form=OffenceForm(request.POST)
                
                if offence_form.is_valid():
                        offence_form.save()
                        message= "Offence Added Successfully"
        else:
                offence_form = OffenceForm()
        offences = Offence.objects.all()
                
        context={
                'form': offence_form,
                'msg': message,
                'offences': offences
        }
        return render(request, "add_offence.html", context)

#select * from crime
# crime.object.get (pk=2) pk is the same as id

@login_required
def edit_criminal_view(request, criminal_id):
        message = ''
        criminal = Criminal.objects.get(id=criminal_id)

        if request.method == "POST":
                criminal_form =CriminalForm(request.POST, instance =criminal)

                if criminal_form.is_valid():
                        criminal_form.save()
                        message = "changes saved sucessfully!"
                else: 
                        message = "form has invalid data"
                        return redirect(add_criminal_view)
        else:
                        criminal_form =CriminalForm(instance=criminal)
        context ={
                'form': criminal_form,
                'criminal': criminal,
                'message': message
        }
        return render(request, 'edit_criminal.html', context)


@login_required
def edit_crime_view(request, crime_id):
        message = ''
        crime = Crime.objects.get(id=crime_id)

        if request.method == "POST":
                crime_form =CrimeForm(request.POST, instance =crime)

                if crime_form.is_valid():
                        crime_form.save()
                        message = "changes saved sucessfully!"
                        return redirect(add_crime_view)
                else: 
                        message = "form has invalid data"
        else:
                        crime_form =CrimeForm( instance=crime)
        context ={
                'form': crime_form,
                'crime': crime,
                'message': message,
        }
        return render(request, 'edit_crime.html', context)


@login_required
def edit_casuality_view(request, casuality_id):
        message = ''
        casuality= Casuality.objects.get(id=casuality_id)

        if request.method == "POST":
                casuality_form =CasualityForm( request.POST, instance =casuality)

                if casuality_form.is_valid():
                        casuality_form.save()
                        message = "changes saved sucessfully!"
                        return redirect(add_Casuality_view)
                else: 
                        message = "form has invalid data"
        else:
                        casuality_form =CasualityForm(request.POST, instance=casuality)
        context ={
                'form': casuality_form,
                'casuality': casuality,
                'message': message,
        }
        return render(request, 'edit_casuality.html', context)

@login_required
def edit_witness_view(request, witness_id):
        message = ''
        witness = Witness.objects.get(id = witness_id)

        if request.method == "POST":
                witness_form =WitnessForm(request.POST, instance =witness)

                if witness_form.is_valid():
                        witness_form.save()
                        message = "changes saved sucessfully!"
                        return redirect(add_witness_view)
                else: 
                        message = "form has invalid data"
        else:
                        witness_form =WitnessForm(request.POST, instance=witness)
        context ={
                'form': witness_form,
                'witness': witness,
                'message': message
        }
        return render(request, 'edit_witness.html', context)

@login_required
def edit_offence_view(request, offence_id):
        message = ''
        offence = Offence.objects.get(id=offence_id)

        if request.method == "POST":
                offence_form =OffenceForm(request.POST, instance =offence)

                if offence_form.is_valid():
                        offence_form.save()
                        message = "changes saved sucessfully!"
                        return redirect(add_Offence_view)
                else: 
                        message = "form has invalid data"
        else:
                        offence_form =OffenceForm(request.POST, instance=offence)
        
        context ={
                'form': offence_form,
                'offence': offence,
                'message': message
        }

        return render(request, 'edit_offence.html', context)

# delete

@login_required
def delete_criminal_view(request, criminal_id):
    criminal = Criminal.objects.get(id = criminal_id)

    criminal.delete()

    return redirect(add_criminal_view)

@login_required
def delete_crime_view(request, crime_id):
    crime = Crime.objects.get(id = crime_id)

    crime.delete()

    return redirect(add_crime_view)

@login_required
def delete_casuality_view(request, casuality_id):
    casuality = Casuality.objects.get(id = casuality_id)

    casuality.delete()

    return redirect(add_casuality_view)

@login_required
def delete_witness_view(request, witness_id):
    witness = Witness.objects.get(id = witness_id)

    witness.delete()

    return redirect(add_witness_view)

@login_required
def delete_offence_view(request, offence_id):
    offence = Offence.objects.get(id = offence_id)

    offence.delete()

    return redirect(add_offence_view)

def sign_up_view (request):
        message = ''
        if request.method=="POST":
                sign_up_form = UserCreationForm(request.POST)
                if sign_up_form.is_valid():
                        sign_up_form.save()
                        message='user created successfully'
                else:
                        message='something went wrong'
        
        sign_up_form = UserCreationForm()

        context = {
                'form': sign_up_form,
                'message':message,
        }
        
        return render(request, 'registration/sign_up.html', context)







