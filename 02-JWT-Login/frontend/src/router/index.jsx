import { BrowserRouter, Routes, Route } from "react-router-dom";
import { LoginPage, RegisterPage, NotFoundPage, HomePage } from "../pages";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route>
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="*" element={<NotFoundPage />} />
          <Route path="/home" element={<HomePage/>}/>
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
