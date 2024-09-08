import express from "express";
import { api as routerApi } from "./router/product.routes.js";


const app = express();
const port = 3000;

app.use(`/api/v1`, routerApi);

try {
  app.listen(port, () => {
    console.log(`Mi Backend esta funcionando 🔥🎉🦾`);
    console.log(`http://localhost:${port}/`);
  });
} catch (error) {
  console.log(error);
}
