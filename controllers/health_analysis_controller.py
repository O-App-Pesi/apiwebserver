from flask import Blueprint, request
from init import db
from models.health_analysis import HealthAnalysis, health_analysis_schema, ha_schema
from flask_jwt_extended import get_jwt_identity, jwt_required

health_analysis_bp = Blueprint('health_analysis', __name__, url_prefix='/healthanalysis')

@health_analysis_bp.route('/')
def get_all_ha():
    stmt = db.select(HealthAnalysis)
    ha = db.session.scalars(stmt) #multiple scalars
    return ha_schema.dump(ha)