import { jwtDecode } from "jwt-decode";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

const HomePage = () => {
   const navigate = useNavigate();

   const imageUrl = "https://cataas.com/cat?type=square";
 
   // Verifica si el token está expirado
   const isTokenExpired = (token) => {
     try {
       const decoded = jwtDecode(token);
       const now = Date.now() / 1000;
       // Voy a saber si mi token expiro o no
       return decoded.exp < now;  // false
     } catch (error) {
       return true;  // Si hay un error al decodificar el token, lo consideramos expirado
     }
   };
 
   // Maneja la solicitud para refrescar el token
   const refreshAccessToken = async () => {
     try {
       const refreshToken = localStorage.getItem("refreshToken");
       const response = await fetch("http://localhost:8000/api/token/refresh/", {
         method: "POST",
         headers: {
           "Content-Type": "application/json",
         },
         body: JSON.stringify({ refresh: refreshToken }),
       });
 
       if (!response.ok) {
         throw new Error("Error al refrescar el token");
       }
 
       const data = await response.json();
       localStorage.setItem("accessToken", data.access);
     } catch (error) {
       console.error("Error al refrescar el token:", error);
       navigate("/login");  // Redirige al usuario al login si hay un error al refrescar el token
     }
   };
 
   useEffect(() => {
     const token = localStorage.getItem("accessToken");
     if (!token || isTokenExpired(token)) {  // Verifica si el token está ausente o expirado
       refreshAccessToken();  // Intenta refrescar el token
     } 
     const refreshToken = localStorage.getItem("refreshToken")
     if (isTokenExpired(refreshToken)){
      localStorage.removeItem("accessToken")
      localStorage.removeItem("refreshToken")
      navigate("/login");
     }
   }, [navigate]);

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 text-gray-800">
      <h1 className="text-9xl font-extrabold tracking-widest text-gray-900">
        HOME PAGE
      </h1>
      <h2>Estamos en construccion</h2>
      <img src={imageUrl} alt="Cat" className="mt-4 rounded-xl" />
    </div>
  );
};

export default HomePage;
