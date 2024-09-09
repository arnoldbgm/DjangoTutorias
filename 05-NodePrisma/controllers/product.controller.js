import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export const getProduct = async (req, res) => {
  //Con esta funcion nostros obtenemos todos los registros de una bd
  const productsRes = await prisma.producto.findMany();
  return res.json({
    msg: "Esta es la data encontrada",
    data: productsRes,
  });
};

export const getCategorias = async (req, res) => {
  // await    prisma.TABLA.METODO
  // El findMany devuelve todos los registros
  const resCategoria = await prisma.categoria.findMany();
  return res.json({
    data: resCategoria,
  });
};

// Crear una consulta que liste todos los productos de una categoria especifica
export const getProductCat = async (req, res) => {
  // api/v1/productoscat?catego=Ropa

  // variable
  // catego = Ropa
  const { catego } = req.query;

  try {
    const resCategoria = await prisma.categoria.findFirst({
      where: {
        nombre: catego,
      },
      include: {
        productos: true,
      },
    });
    return res.json(resCategoria.productos);
  } catch (error) {
    console.log(error);
    return;
  }
};

// Crear una consulta que ordene el precio de los productos de mayor a menor

// api/v1/productosorden?order=asc
export const getProductOrder = async (req, res) => {
  let { order = "asc" } = req.query;

  if (order !== "desc") {
    order = "asc";
  }

  try {
    const getProducts = await prisma.producto.findMany({
      orderBy: {
        // Aqui especifico que columna se va ordenar
        precio: order,
      },
    });
    res.json(getProducts);
  } catch (error) {
    console.log(error);
    return;
  }
};

// Crear una consulta que me traiga los productos por su nombre
export const getProductName = async (req, res) => {
  // api/v1/productosnombre?nombre=mouse
  // mouse  MOUSE  mOuSe

  const { nombre } = req.query;

  try {
    const getProductoN = await prisma.producto.findMany({
      where: {
        nombre: {
          contains: nombre,
          mode: "insensitive",
        },
      },
    });

    res.json(getProductoN);
  } catch (error) {
    console.log(error);
    return;
  }
};

export const getProductPagination = async (req, res) => {
  // api/v1/getproduct
  const { page = 1, pageSize = 5 } = req.query;

  const skip = (page - 1) * pageSize;

  try {
    const dataProduct = await prisma.producto.findMany({
      // Aqui vamos a usar la paginacion
      skip: parseInt(skip),
      take: parseInt(pageSize), //Cuantos productos quiero que se meuestre por pagina
      orderBy:{
        id: "asc"
      }
    });
    res.json(dataProduct);
  } catch (error) {
    console.log(error);
    return;
  }
};
