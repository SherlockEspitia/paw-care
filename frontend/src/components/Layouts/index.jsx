import './Layout.css'
import { Header, Footer} from '@/components'

const Layout= ({children})=>{
    return(
        <>
            <Header/>
            <main>{children}</main>
            <Footer/>
        </>
    )
}

export default Layout