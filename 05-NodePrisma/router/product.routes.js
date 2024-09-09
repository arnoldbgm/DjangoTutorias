import { Router } from "express";

import {
  getCategorias,
  getProduct,
  getProductCat,
  getProductName,
  getProductOrder,
  getProductPagination,
} from "../controllers/product.controller.js";

// Esta parte nos permite exportar nuestra funcion
export const api = Router();

// Aqui estamos declarando la url y asociandolo a un controlador
api.get("/productos", getProduct);
api.get("/categorias", getCategorias);
api.get("/productoscat", getProductCat);
api.get("/productoprice", getProductOrder);
api.get("/productosnombre", getProductName);
api.get("/allproduct", getProductPagination)