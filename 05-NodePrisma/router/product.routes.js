import { Router } from "express";

import { getProduct } from "../controllers/product.controller.js";

// Esta parte nos permite exportar nuestra funcion
export const api = Router();

// Aqui estamos declarando la url y asociandolo a un controlador
api.get("/productos", getProduct);