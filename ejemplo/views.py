from django.shortcuts import render, get_object_or_404

from ejemplo.models import Familiar

from ejemplo.forms import Buscar, AmigosForm

from ejemplo.forms import Buscar, FamiliarForm

from ejemplo.forms import Buscar, ClientesForm

from django.views import View 

from ejemplo.forms import Buscar

from ejemplo.models import Amigo

from ejemplo.models import Cliente

from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView



def index(request):
    return render(request, "ejemplo/saludar.html")


def saludar_a(request, nombre):
    return render(request, 
    'ejemplo/saludar_a.html',
    {'nombre': nombre}
    )


def sumar(request, a, b):
    return render (request,
    'ejemplo/sumar.html',
    {'a': a,
    'b': b,
    'resultado' : a + b
    }
    )


def buscar(request):
    lista_de_nombre = ["German", "Daniel", "Romero", "Alvaro"]
    query =request.GET['q']
    if query in lista_de_nombre:
        indice_de_resultado = lista_de_nombre.index(query)
        resultado = lista_de_nombre[indice_de_resultado]
    else:
        resultado = "no hay match"

    return render(request, 'ejemplo/buscar.html', {"resultado": resultado})


def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})


class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actualizar_familiar.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})



class BorrarFamiliar(View):
  template_name = 'ejemplo/familiar.html'
    
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      familiar.delete()
      familiares = Familiar.objects.all()
      return render(request, self.template_name, {'lista_familiares': familiares})


def mostrar_Amigos(request):
  lista_Amigos = Amigo.objects.all()
  return render(request, "ejemplo/Amigos.html", {"lista_Amigos": lista_Amigos})


class AltaAmigo(View):

    form_class = AmigosForm
    template_name = 'ejemplo/alta_Amigo.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el Amigo {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})



class BuscarAmigo(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar_amigos.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_Amigos = Amigo.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_Amigos':lista_Amigos})
        return render(request, self.template_name, {"form": form})


def mostrar_Clientes(request):
  lista_Clientes = Cliente.objects.all()
  return render(request, "ejemplo/Clientes.html", {"lista_Clientes": lista_Clientes})

class AltaCliente(View):

    form_class = ClientesForm
    template_name = 'ejemplo/alta_Cliente.html'
    initial = {"nombre":"", "direccion":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el Cliente {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})


class BuscarCliente(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar_clientes.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_Clientes = Cliente.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_Clientes':lista_Clientes})
        return render(request, self.template_name, {"form": form})

class ActualizarAmigo(View):
  form_class = AmigosForm
  template_name = 'ejemplo/actualizar_Amigos.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  
  def get(self, request, pk): 
      Amigo = get_object_or_404(Amigo, pk=pk)
      form = self.form_class(instance=Amigo)
      return render(request, self.template_name, {'form':form,'Amigo': Amigo})

 
  def post(self, request, pk): 
      Amigo = get_object_or_404(Amigo, pk=pk)
      form = self.form_class(request.POST ,instance=Amigo)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el Amigo {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'Amigo': Amigo,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class ActualizarCliente(View):
  form_class = ClientesForm
  template_name = 'ejemplo/actualizar_Cliente.html'
  initial = {"nombre":"", "direccion":""}
  
  
  def get(self, request, pk): 
      Cliente = get_object_or_404(Cliente, pk=pk)
      form = self.form_class(instance=Cliente)
      return render(request, self.template_name, {'form':form,'Cliente': Cliente})

  
  def post(self, request, pk): 
      Cliente = get_object_or_404(Cliente, pk=pk)
      form = self.form_class(request.POST ,instance=Cliente)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el Cliente {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'Cliente': Cliente,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})


class FamiliarList(ListView):
  model = Familiar

class FamiliarCrear(CreateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "numero_pasaporte"]


class FamiliarBorrar(DeleteView):
  model = Familiar
  success_url = "/panel-familia"

class FamiliarActualizar(UpdateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "numero_pasaporte"]  

class FamiliarActualizar(UpdateView):
    model = Familiar
    success_url = "/success_updated_message.html"
    fields = ["nombre", "direccion", "numero_pasaporte"]  

class FamiliarDetalle(DetailView):
  model = Familiar