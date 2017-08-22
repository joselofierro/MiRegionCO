from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# si no estoy autentificado me manda al login
def index(request):
    if request.user.is_authenticated():
        return redirect('noticia:listar_noticia')
    else:
        return redirect('grupo:login')


def login_view(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        password = request.POST['password']
        user_auth = authenticate(username=usuario, password=password)
        # si el usuario esta autentificado y activado
        if user_auth is not None:
            if user_auth.is_active:
                # lo dejan ingresar
                login(request, user_auth)
                if user_auth.groups.filter(name='Escritor').exists() or user_auth.groups.filter(name='SupervisorEscritor').exists():
                    return redirect('noticia:listar_noticia')

                elif user_auth.groups.filter(name='Administrador').exists():
                    return redirect('noticia:listar_noticia')

                elif user_auth.groups.filter(name='SupervisorVendedor').exists():
                    return redirect('cotizacion:listar_cotizacion')
            else:
                return render(request, 'index.html', {'error': 'Usuario no activo'}, content_type='text/html')
        else:
            return render(request, 'index.html', {'error': 'Datos incorrectos'}, content_type='text/html')
    else:
        return render(request, 'index.html', {}, content_type='text/html')


def logout_view(request):
    logout(request)
    return redirect('grupo:login')
