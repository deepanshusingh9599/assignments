from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from .helpers import default_response, serializer_error_format
import traceback
from django.core.paginator import Paginator
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class ProductsAPIView(APIView):
    '''
    API View for CRUD operations on Product Model
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        '''
           Method for retrieving the all product data and particular record
        '''
        try:
            product_id = request.query_params.get('product_id', None)
            if product_id is None:
                '''
                Scope for all product's data
                '''
                page_no = request.query_params.get('page', 1)
                limit = request.query_params.get('limit', 10)

                product_objs = Product.objects.all()
                product_data = ProductSerializer(product_objs, many=True
                                                 )
                total_count = len(product_data.data)
                try:
                    paginator = Paginator(product_data.data, limit)
                except:
                    return Response(default_response(
                        success=False,
                        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        message="Limit parameter must be an integer!",
                        result={},
                        error={
                            "error": "Provided limit parameter has wrong value, must be an integer.",
                            "message_code": "PROVIDED_WRONG_LIMIT"
                        }
                    ), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
                try:
                    obj = paginator.page(page_no)
                    previous_page = obj.previous_page_number() if obj.has_previous() else None
                    next_page = obj.next_page_number() if obj.has_next() else None
                except Exception as e:
                    return Response(default_response(
                        success=False,
                        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        message="Page parameter must be an integer!",
                        result={},
                        error={
                            "error": "Provided page parameter has wrong value, must be an integer.",
                            "message_code": "PROVIDED_WRONG_PAGE_NO"
                        }
                    ), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
                return Response(default_response(
                    success=True,
                    status_code=status.HTTP_200_OK,
                    message="All Products fetched successfully.",
                    result={
                        "total_count": total_count,
                        "previous_page": previous_page,
                        "next_page": next_page,
                        "data": list(obj)
                    },
                    error={}
                ), status=status.HTTP_200_OK)
            else:
                '''
                 Scope for specific product's data
                '''
                try:
                    product_obj = Product.objects.get(id=int(product_id))

                except ValueError:
                    return Response(default_response(
                        success=False,
                        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        message="Product id must be an integer!",
                        result={},
                        error={
                            "error": "Provided product id has wrong value, must be an integer.",
                            "message_code": "PROVIDED_WRONG_PRODUCT_ID"
                        }
                    ), status=status.HTTP_422_UNPROCESSABLE_ENTITY)

                except Product.DoesNotExist:
                    return Response(default_response(
                        success=False,
                        status_code=status.HTTP_404_NOT_FOUND,
                        message="Product does not exist with the given id!",
                        result={},
                        error={
                            "error": "Product does not exist.",
                            "message_code": "PRODUCT_DOES_NOT_EXIST"
                        }
                    ), status=status.HTTP_404_NOT_FOUND)
                product_data = ProductSerializer(product_obj)
                return Response(default_response(
                    success=True,
                    status_code=status.HTTP_200_OK,
                    message="Product fetched successfully.",
                    result={
                        "data": product_data.data
                    },
                    error={}
                ), status=status.HTTP_200_OK)

        except Exception as e:
            print("--------------------------traceback exceptional error-------------------------------")
            traceback.print_exc()
            print("------------------------------------------------------------------------------------")
            return Response(default_response(
                success=False,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message="Internal process failed",
                result={},
                error={
                    "error": repr(e),
                    "message_code": "INTERNAL_PROCESS_FAILED"
                }
            ), status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        '''
         Method for creating new product record.
        '''
        try:
            try:
                data = request.data
            except ParseError as e:
                return Response(default_response(
                    success=False,
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    message="Wrong data provide in the JSON body",
                    result={},
                    error={
                        "error": "Provided wrong data in JSON body",
                        "message_code": "PROVIDED_WRONG_JSON_DATA"
                    }
                ), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            product_ser = ProductSerializer(data=data)

            if product_ser.is_valid():
                product_ser.save()
                return Response(default_response(
                    success=True,
                    status_code=status.HTTP_201_CREATED,
                    message="Product created successfully.",
                    result=product_ser.data,
                    error={}
                ), status.HTTP_201_CREATED)
            else:
                serializer_error = serializer_error_format(product_ser.errors)
                return Response(default_response(
                    success=False,
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    message="Field validation failed.",
                    result={},
                    error={
                        "error": serializer_error,
                        "message_code": "FIELD_VALIDATION_FAILED"
                    }
                ), status.HTTP_422_UNPROCESSABLE_ENTITY)

        except Exception as e:
            print("--------------------------traceback exceptional error-------------------------------")
            traceback.print_exc()
            print("------------------------------------------------------------------------------------")
            return Response(default_response(
                success=False,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message="Internal process failed",
                result={},
                error={
                    "error": repr(e),
                    "message_code": "INTERNAL_PROCESS_FAILED"
                }
            ), status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        '''
         Method for updating any specific product's record data
        '''
        try:
            try:
                data = request.data
            except ParseError as e:
                return Response(default_response(
                    success=False,
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    message="Wrong data provide in the JSON body",
                    result={},
                    error={
                        "error": "Provided wrong data in JSON body",
                        "message_code": "PROVIDED_WRONG_JSON_DATA"
                    }
                ), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            product_id = data.get('id')

            try:
                product_obj = Product.objects.get(id=product_id)

            except ValueError:
                return Response(default_response(
                    success=False,
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    message="Product id must be an integer!",
                    result={},
                    error={
                        "error": "Provided product id has wrong value, must be an integer.",
                        "message_code": "PROVIDED_WRONG_PRODUCT_ID"
                    }
                ), status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            except Product.DoesNotExist:
                return Response(default_response(
                    success=False,
                    status_code=status.HTTP_404_NOT_FOUND,
                    message="Product does not exist with the given id!",
                    result={},
                    error={
                        "error": "Product does not exist.",
                        "message_code": "PRODUCT_DOES_NOT_EXIST"
                    }
                ), status=status.HTTP_404_NOT_FOUND)

            product_ser = ProductSerializer(instance=product_obj, data=data)

            if product_ser.is_valid():
                product_ser.save()
                return Response(default_response(
                    success=True,
                    status_code=status.HTTP_200_OK,
                    message="Product updated successfully.",
                    result=product_ser.data,
                    error={}
                ), status.HTTP_200_OK)
            else:
                serializer_error = serializer_error_format(product_ser.errors)
                return Response(default_response(
                    success=False,
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    message="Field validation failed.",
                    result={},
                    error={
                        "error": serializer_error,
                        "message_code": "FIELD_VALIDATION_FAILED"
                    }
                ), status.HTTP_422_UNPROCESSABLE_ENTITY)

        except Exception as e:
            print("--------------------------traceback exceptional error-------------------------------")
            traceback.print_exc()
            print("------------------------------------------------------------------------------------")
            return Response(default_response(
                success=False,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message="Internal process failed",
                result={},
                error={
                    "error": repr(e),
                    "message_code": "INTERNAL_PROCESS_FAILED"
                }
            ), status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        '''
         Method for deleting any specific product's record data.
        '''
        try:
            try:
                data = request.data
            except ParseError as e:
                return Response(default_response(
                    success=False,
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    message="Wrong data provide in the JSON body",
                    result={},
                    error={
                        "error": "Provided wrong data in JSON body",
                        "message_code": "PROVIDED_WRONG_JSON_DATA"
                    }
                ), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            product_id = data.get('id')

            try:
                product_obj = Product.objects.get(id=product_id)

            except ValueError:
                return Response(default_response(
                    success=False,
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    message="Product id must be an integer!",
                    result={},
                    error={
                        "error": "Provided product id has wrong value, must be an integer.",
                        "message_code": "PROVIDED_WRONG_PRODUCT_ID"
                    }
                ), status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            except Product.DoesNotExist:
                return Response(default_response(
                    success=False,
                    status_code=status.HTTP_404_NOT_FOUND,
                    message="Product does not exist with the given id!",
                    result={},
                    error={
                        "error": "Product does not exist.",
                        "message_code": "PRODUCT_DOES_NOT_EXIST"
                    }
                ), status=status.HTTP_404_NOT_FOUND)

            product_name = product_obj.name
            product_deleted, _ = product_obj.delete()

            if product_deleted:
                return Response(default_response(
                    success=True,
                    status_code=status.HTTP_200_OK,
                    message=f"Product '{product_name}' with id '{str(product_id)}' deleted successfully.",
                    result={},
                    error={}
                ), status.HTTP_200_OK)

        except Exception as e:
            print("--------------------------traceback exceptional error-------------------------------")
            traceback.print_exc()
            print("------------------------------------------------------------------------------------")
            return Response(default_response(
                success=False,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message="Internal process failed",
                result={},
                error={
                    "error": repr(e),
                    "message_code": "INTERNAL_PROCESS_FAILED"
                }
            ), status.HTTP_500_INTERNAL_SERVER_ERROR)
