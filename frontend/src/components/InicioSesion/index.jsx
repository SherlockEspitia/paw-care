import React from 'react'
import './InicioSesion.css'


export const InicioSesion = () => {
    return (
        <main className="auth">
            <section className="card" role="form" aria-labelledby="titulo-form">
                <h1 id="titulo-form">Inicia sesión</h1>

                <form action="#" method="post" noValidate>
                    <div className="field">
                        <label htmlFor="email">Usuario</label>
                        <input
                            id="email"
                            name="email"
                            type="email"
                            inputMode="email"
                            autoComplete="email"
                            placeholder="tucorreo@ejemplo.com"
                            required
                        />
                    </div>

                    <div className="field">
                        <label htmlFor="password">Contraseña</label>
                        <input
                            id="password"
                            name="password"
                            type="password"
                            autoComplete="current-password"
                            minLength="6"
                            placeholder="Tu contraseña"
                            required
                        />
                    </div>

                    <div className="row">
                        <label className="check">
                            <input type="checkbox" name="remember" />
                            <span>Recordarme</span>
                        </label>

                        <a className="link" href="#" title="Recuperar contraseña">
                            ¿Olvidaste tu contraseña?
                        </a>
                    </div>

                    <button className="btn" type="submit">
                        Ingresar
                    </button>
                </form>

                <p className="legal">
                    Al continuar, aceptas nuestros{" "}
                    <a className="link" href="#">
                        Términos
                    </a>{" "}
                    y{" "}
                    <a className="link" href="#">
                        Política de privacidad
                    </a>
                    .
                </p>
            </section>
        </main>
    )
}

export default InicioSesion
