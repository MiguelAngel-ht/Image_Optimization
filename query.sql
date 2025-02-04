
select distinct 
    a.prdClave, prdCode, flxImagen_Alternativa -- flxImagen_Producto  -- flxImagen_Alternativa
from 
    Temporales.dbo.Flex_Imagenes_v2 as a
left join bdc.dbo.catProducto as b on b.prdClave = a.prdClave 
where 
    a.prdClave in (select distinct prdClave 
                    from Temporales_RESP.dbo.ORA2_PRONOSTICO_SIMILARES_XUDN_TALLA
                    where id_proyecto = (SELECT ID_Proyecto from Temporales_RESP.dbo.ORA2_PROYECTOS_A_EVALUAR_CARGA where ReporteSem = 1) 
                            and [version] = 1)