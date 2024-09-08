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
