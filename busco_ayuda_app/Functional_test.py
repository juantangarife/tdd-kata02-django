__author__ = 'asistente'
from busco_ayuda.wsgi import application
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from busco_ayuda.settings import BASE_DIR
import time
from busco_ayuda_app.models import Trabajador
from django.db.models import Q

def current_milli_time():
    int(round(time.time() * 1000))


class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(os.path.join(BASE_DIR, 'test-resources', 'chromedriver'))
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Juan Daniel')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Arevalo')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3173024578')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jd.patino1@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys(os.path.join(BASE_DIR, 'test-resources', 'best-places-for-web-developer-jobs.jpg'))

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('juan645' + str(current_milli_time()))

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', span.text)

    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', h2.text)

    def test_login(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        username = self.browser.find_element_by_id('id_login_username')
        username.send_keys('juan645')

        password = self.browser.find_element_by_id('id_login_password')
        password.send_keys('clave123')

        boton_login = self.browser.find_element_by_id('id_login_boton')
        boton_login.click()
        self.browser.implicitly_wait(3)

        message = self.browser.find_element_by_id('id_messages')
        self.assertIn('Bienvenido al sistema', message.text)

    def test_editar(self):
        self.browser.get('http://localhost:8000/editar/2')

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys(' updated')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys(' updated')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('2')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('.com')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys(os.path.join(BASE_DIR, 'test-resources', 'best-places-for-web-developer-jobs.jpg'))

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)

        message = self.browser.find_element_by_id('id_messages')
        self.assertIn('Su perfil fue actualizado correctamente', message.text)

    def test_comentario(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()
        self.browser.implicitly_wait(3)

        correo_temp = 'juan645' + str(current_milli_time()) + '@gmail.com'
        correo = self.browser.find_element_by_id('correo')
        correo.send_keys(correo_temp)

        comentario_temp = 'Soy el comentario' + str(current_milli_time())
        comentario = self.browser.find_element_by_id('comentario')
        comentario.send_keys(comentario_temp)

        boton_comentario = self.browser.find_element_by_id('id_comentario_button')
        boton_comentario.click()
        self.browser.implicitly_wait(3)

        correo_new = self.browser.find_element_by_class_name('correo-detail')
        comnetario_new = self.browser.find_element_by_class_name('comentario-detail')

        self.assertEquals(correo_temp, correo_new.text,
                          "Comparacion de correos en la funcionalida de adicion comentarios")
        self.assertEquals(comentario_temp, comnetario_new.text,
                          "Comparacion de comentarios en la funcionalida de adicion comentarios")

    def test_buscar_trabajador(self):
        self.browser.get('http://localhost:8000')
        buscar = self.browser.find_element_by_id('buscar')
        buscar.send_keys('arevalo')
        boton = self.browser.find_element_by_id('boton-buscar-trabajador')
        boton.click()
        self.browser.implicitly_wait(3)
        results = self.browser.find_elements_by_class_name('nombre-servicio')
        query = Trabajador.objects.filter(Q(nombre__icontains ='arevalo') | Q(apellidos__icontains='arevalo'))
        self.assertEquals(len(results), query.count(), 'Numero de trabajadores por nombre/apellido')
