__author__ = 'asistente'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from busco_ayuda.settings import BASE_DIR
import time
current_milli_time = lambda: int(round(time.time() * 1000))


class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(os.path.join(BASE_DIR, 'test-resources', 'chromedriver.exe'))
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

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3173024578')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jd.patino1@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys(os.path.join(BASE_DIR, 'test-resources', 'best-places-for-web-developer-jobs.jpg'))

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('juan645'+str(current_milli_time()))

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', span.text)

    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span=self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()

        h2=self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')

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
