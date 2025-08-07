# 🛣️ Censo Vial y Seguridad - SMA

Aplicación web desarrollada con **FastAPI** para el registro y monitoreo de la situación de carreteras, condiciones climáticas, orden público y noticias relevantes. Dirigida a funcionarios de campo y analistas de seguridad física en el sector petrolero.

---

## 🚀 Características principales

- ✅ Registro de eventos en tiempo real desde dispositivos móviles
- ✅ Consulta de datos por región, tipo de evento y fecha
- ✅ Integración con APIs externas para clima, noticias y orden público
- ✅ Panel administrativo para validación y análisis de datos

---

## 🧰 Tecnologías utilizadas

- Python 3.11  
- FastAPI  
- SQLite / PostgreSQL  
- Bootstrap / Tailwind CSS  
- GitHub Actions (CI/CD)  
- Docker (opcional)  

---

## 📦 Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/EdgarJavierDiaz/censo-vial-sma.git
   cd censo-vial-sma
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv env
   source env/bin/activate      # En Linux/Mac
   .\env\Scripts\activate       # En Windows
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta la aplicación:

   ```bash
   uvicorn main:app --reload
   ```

---

## 📡 Endpoints principales

| Método | Endpoint            | Descripción                         |
|--------|---------------------|-------------------------------------|
| GET    | `/eventos`          | Lista de eventos registrados        |
| POST   | `/eventos`          | Registro de nuevo evento            |
| GET    | `/clima`            | Consulta de clima por región        |
| GET    | `/noticias`         | Noticias relevantes del día         |
| GET    | `/orden-publico`    | Situación de orden público actual   |

---

## 🧪 Pruebas

Para ejecutar las pruebas, puedes usar `pytest`:

```bash
pytest
```

(Agrega más detalles aquí si tienes tests específicos o configuración de pruebas)

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!  
Puedes seguir estos pasos para contribuir:

1. Haz un fork del repositorio
2. Crea una rama (`git checkout -b feature/nueva-feature`)
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva feature'`)
4. Haz push a tu rama (`git push origin feature/nueva-feature`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## 📫 Contacto

**Edgar Javier Díaz**  
[GitHub](https://github.com/EdgarJavierDiaz)  
Correo: *(agrega tu email si deseas)*
