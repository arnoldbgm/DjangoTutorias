## Configuración del proyecto de express

Partidos todo empezando por ejecutar el siguiente comando

```bash
npm init
```

Ahora instalamos  ***express***

```bash
npm install express
```

Ahora instalamos ***nodemon***

```bash
npm install --save-dev nodemon
```

Para este punto nuestro ***package.json*** debe lucir asi:

```json
{
  "name": "tutoria_express",
  "version": "1.0.0",
  "description": "Este sera el backend de mi proyecto final",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.19.2"   //ESTO ES EXPRESS
  },
  "devDependencies": {
    "nodemon": "^3.1.4"   //ESTO ES NODEMON
  }
}
```

Ahora para poder usar nodemon debemos de hacer un cambio en el package.json, debemos colocar  `“dev” : “nodemon app.js”`  Esto hara que cada vez que queramos levantar nuestro backend solo debamos de colocar en terminal `npm run dev` , tambien debemos de colocar el   `"type": "module",`

```json
{
  "name": "tutoria_express",
  "version": "1.0.0",
  "description": "Este sera el backend de mi proyecto final",
  "type": "module",     // Esto hemos agregado
  "main": "index.js", 
  "scripts": {
    "dev": "nodemon app.js",  // Esto es para trabajar con nodemon
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.19.2"
  },
  "devDependencies": {
    "nodemon": "^3.1.4"
  }
}
```

Una vez hecho todo esto pasamos a crear el archivo`app.js`, si lo vez esta en la raiz a la misma altura que mi `package.json`

![image](https://github.com/user-attachments/assets/76177d42-bf88-4024-8be1-c3219ddedad0)

Ahora dentro del archivo **`app.js`**, copiamos  y pegamos el siguiente codigo

```jsx
import express from "express";

// Aqui inicializo mi aplicacion en express
const app = express();
// Este sera el puerto que va a usar mi backend
const port = 3000;

// Aqui se ejecutara mi backend
// Esta parte solo se crea una vez y una vez ya configurada no se vuelve a tocar
try {
  app.listen(port, () => {
    console.log(`Mi Backend esta funcionando 🔥🎉🦾 `);
    console.log(`http://localhost:${port}/`);
  });
} catch (error) {
  console.log(error);
}
```

Con que te vayas a la terminal y ejecutes `npm run dev`, habras logrado levantar tu backend usando express

![image](https://github.com/user-attachments/assets/0671df69-1d80-48e7-9fa8-fc74666c67f3)

## Creación de nuestra Base de datos

Para comenzar con la creación de nuestra Bd, es importante que tengamos instalado prisma dentro de nuestro proyecto, por lo que ejecutaremos el siguiente comando

```bash
npm install prisma --save-dev
```

Ahora ejecutaremos lo siguiente, para poder instalar Prisma ORM 

```bash
npx prisma init 
```

Veremos que se nos crearon una carpeta llamada `prisma` y `.env` , no tengas miedo

![image](https://github.com/user-attachments/assets/57c7c0cc-e6f7-4f5b-8b33-f1e3ba10f8c5)

<aside>
💡 Es fundamental que comprendas que dentro de la carpeta de `prisma` es donde crearemos nuestra base de datos. El archivo `.env` nos permite especificar la ubicación de nuestra base de datos.

</aside>

🔥 ***IMPORTANTE (usaremos MYSQL) :  Ahora nos iremos a mysqlworkbech y crearemos desde ahi una bd, con el comando*** 

```sql
CREATE DATABASE IF NOT exists mi_base_de_datos;
```

<aside>
💡 Lo que hize aqui es crear una base de datos con el `nombe mi_base_de_datos`

</aside>

Ahora me ire al archivo `.env` para configurarlo, pero antes de configurarlo, este es el protocolo de como se configura 

![image](https://github.com/user-attachments/assets/74ae6456-ed3b-48aa-81a1-12b7221b2327)

```jsx
//Esto significa que solo debo de cambiar =>  mysql://USER:PASSWORD@HOST:PORT/DATABASE

// Asi es como nos viene por defecto
DATABASE_URL="postgresql://johndoe:randompassword@localhost:5432/mydb?schema=public"
 
// Pero debemos de cambiarlo por nuestro BD, USER, PASSWORD, HOST , PORT , DATABASE
// Asi seria en mi caso

DATABASE_URL="mysql://root:root@localhost:3306/mi_base_de_datos"   👍
```

Genial, ahora vamos, a la carpeta prisma donde cambiaremos el provider

```jsx
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "mysql"  // esto viene por defecto postgresql, solo lo cambiamos
  url      = env("DATABASE_URL")
}

model Categoria {
  id        Int      @id @default(autoincrement())
  nombre    String
  productos Producto[]
}

// Definición del modelo de Producto
model Producto {
  id          Int       @id @default(autoincrement())
  nombre      String
  descripcion String?
  precio      Float
  categoriaId Int
  categoria   Categoria @relation(fields: [categoriaId], references: [id])
}
```

Lo que hicimos fue modelar la siguiente base de datos.

![image](https://github.com/user-attachments/assets/02fed100-159b-4e0c-86b3-757d53460155)


Si tu vas y a tu mysql workbech veras que no tienes ninguna tabla y que tu base de datos esta vacia, y esto se debe porque aun no ejecutaste la migracion correspondiente, esta la debes de ejecutar en tu terminal, con esto ya podras observar tu bd.

```bash
npx prisma migrate dev 
```

## Creación de controladores y de rutas

Ahora haremos la creación de las carpetas `controllers` y `router`, tendremos de la siguiente forma nuestro proyecto

![image](https://github.com/user-attachments/assets/ff68edc3-a702-4985-95de-ee62815b5031)

<aside>
💡

### Controllers

En los **controllers**, se definen todas las funciones lógicas relacionadas con nuestras tablas de base de datos. Estas funciones manejan las operaciones CRUD y otras lógicas de negocio necesarias para interactuar con los datos almacenados.

### Routers

En los **routers**, se especifican las rutas específicas para las peticiones HTTP que serán manejadas por nuestra aplicación Express. Cada archivo de enrutador define cómo se responderá a cada tipo de solicitud (GET, POST, PUT, DELETE, etc.) y conecta esas rutas con las funciones correspondientes en los controllers.

</aside>

### Controladores crea el siguiente archivo (`controllers/product.controller.js`)

Aquí es donde colocarás la lógica para manejar las peticiones HTTP relacionadas con los productos.

```jsx
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

// Recuerda iniciar con export para exportar para que se pueda exportar la funcion
export const getProduct = async (req, res) => {
  //Con esta funcion nostros obtenemos todos los registros de una bd
  const productsRes = await prisma.producto.findMany();
  return res.json({
    msg: "Esta es la data encontrada",
    data: productsRes,
  });
};
```

### Rutas crea el siguiente archivo  (`routes/product.routes.js`)

Aquí defines las rutas específicas y las asocia con los controladores correspondientes.

```jsx
import { Router } from "express";
import { getProduct } from "../controllers/product.controller.js";

// Esta parte nos permite instanciar y poder exportar todas nuestras rutas
export const api = Router();

// Aqui estamos declarando la url y asociandolo a un controlador
api.get("/producto", getProduct);
```

### Configuración de Express (`app.js`)

Finalmente, configura tu aplicación Express en `app.js` para usar las rutas definidas.

```jsx
import express from "express";
// Esto es lo nuevo que añadimos para poder usar las rutas que creamos
import { api as routerApi } from "./routes/product.routes.js";

const app = express();
const port = 3000;

// Aqui es donde puedo usar las rutas estoy concatenando
// asi serian mis endpoint http://localhost:3000/api/v1/producto`
app.use(`/api/v1`, routerApi);

app.listen(port, () => {
  console.log(`Mi Backend está funcionando 🔥🎉🦾`);
  console.log(`http://localhost:${port}/`);
});

```

---

## Ejercicios con la ORM

```bash
-- MOCKS PARA POSTGRES
-- Mocks para Categoria
INSERT INTO "Categoria" ("nombre") VALUES
  ('Electrónicos'),
  ('Ropa'),
  ('Hogar');

-- Mocks para Producto
INSERT INTO "Producto" ("nombre", "descripcion", "precio", "categoriaId") VALUES
  ('Smartphone', 'Teléfono inteligente de última generación', 999.99, 1),
  ('Laptop', 'Laptop potente para trabajo y entretenimiento', 1499.99, 1),
  ('Camiseta', 'Camiseta de algodón en varios colores', 19.99, 2),
  ('Mesa', 'Mesa de madera resistente para el comedor', 299.99, 3),
  ('Monitor', 'Monitor LED de alta definición', 299.99, 1),
  ('Teclado mecánico', 'Teclado mecánico RGB para gamers', 79.99, 1),
  ('Mouse inalámbrico', 'Mouse ergonómico sin cables', 29.99, 1),
  ('Pantalones vaqueros', 'Jeans clásicos para hombres', 49.99, 2),
  ('Vestido de noche', 'Vestido elegante para ocasiones especiales', 89.99, 2),
  ('Sofá seccional', 'Sofá cómodo con diseño modular', 799.99, 3),
  ('Mesa de café', 'Mesa auxiliar para la sala de estar', 149.99, 3);
```


```bash
-- MOCKS PARA MYSQL
-- Mocks para Categoria
INSERT INTO Categoria (nombre) VALUES
  ('Electrónicos'),
  ('Ropa'),
  ('Hogar');

-- Mocks para Producto
INSERT INTO Producto (nombre, descripcion, precio, categoriaId) VALUES
  ('Smartphone', 'Teléfono inteligente de última generación', 999.99, 1),
  ('Laptop', 'Laptop potente para trabajo y entretenimiento', 1499.99, 1),
  ('Camiseta', 'Camiseta de algodón en varios colores', 19.99, 2),
  ('Mesa', 'Mesa de madera resistente para el comedor', 299.99, 3);
  ('Monitor', 'Monitor LED de alta definición', 299.99, 1),
  ('Teclado mecánico', 'Teclado mecánico RGB para gamers', 79.99, 1),
  ('Mouse inalámbrico', 'Mouse ergonómico sin cables', 29.99, 1),
  ('Pantalones vaqueros', 'Jeans clásicos para hombres', 49.99, 2),
  ('Vestido de noche', 'Vestido elegante para ocasiones especiales', 89.99, 2),
  ('Sofá seccional', 'Sofá cómodo con diseño modular', 799.99, 3),
  ('Mesa de café', 'Mesa auxiliar para la sala de estar', 149.99, 3);

```
