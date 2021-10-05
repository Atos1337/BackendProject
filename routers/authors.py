from fastapi import APIRouter
from starlette.graphql import GraphQLApp
from gql.schema import schema

router = APIRouter()
router.add_route("/author-stat", GraphQLApp(schema=schema))
