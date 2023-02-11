from typing import Optional , List
from fastapi import APIRouter , Header , Cookie , Form
from fastapi import Response 
from fastapi import status , Depends
from fastapi.responses import PlainTextResponse , HTMLResponse 


router = APIRouter(
    prefix= "/product",
    tags = ["product"]
)

products = ["mirror","sofa","television"]

@router.get("/withheader")
def get_products(response: Response,custom_header: Optional[List[str]] = Header(None)):
    response.headers["custom_response_header"] = " ".join(custom_header)
    return products

@router.get("/all")
def get_all_products():
    #? return products
    data = " ".join(products)
    response = Response(content=data,media_type="text/plain")
    response.set_cookie(key = "test_cookie_title",value="test_cookie_value")
    return {
    "response":response,        
    }


@router.get("/{id}")
def get_product(id: int,test_cookie_title: Optional[str] = Cookie(None)):
    if id > 2:
        output = f"Product with id {id} not found"
        return PlainTextResponse(content=output,media_type="text/plain",status_code=status.HTTP_404_NOT_FOUND)
    product = products[id]
    output = f"""
    <html>
        <body>
        <h1>{product}</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=output,media_type="text/html")  
        
@router.post("/create")
def create_product(name: str = Form(...)):
    products.append(name)
    return products