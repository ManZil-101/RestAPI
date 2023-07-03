
"""Learning CRUD operation and Authentication using RESTAPI"""

---> Function based methods for CRUD 
    using decorator (@APIView('[methods]'))

---> Class based Views from CRUD
    creating all CRUD operation with in single class using differnent methods 
    --> def get()
            pass
    ---> def post()
            pass 
        so on ......

---> Generic view based CRUD operation
    it provide and environment for CRUD operation without implementing own logic for CRUD.
    ---> Using generics modules.
        ---> ListAPIView,
        ---> CreateAPIView
        ---> DestroyAPIView
        ---> RetrieveAPIView
        ---> UpdateAPIView
        ---> RetrieveUpdateAPIView
        ---> RetrieveDestroyAPIView
        ---> RetrieveListAPIView
        ---> RetrieveUpdateDestroyAPIView
        ---> RetrieveUpdateListAPIView
        ---> RetrieveDestroyListAPIView 
        ---> RetrieveUpdateDestroyListAPIView
        so on...

---> Authentication
---> Token based Authentication
---> JWT (JSON Web Token) based Authentication


---> Serializers
    ---> Serializers are used to convert Model Object to json and vice versa
    ---> Serializers are responsible for serializing and deserializing data.





