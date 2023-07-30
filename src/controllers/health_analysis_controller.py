from flask import Blueprint, request
from init import db
from models.health_analysis import HealthAnalysis, health_analysis_schema, ha_schema

health_analysis_bp = Blueprint('health_analysis', __name__, url_prefix='/healthanalysis')

#GET query, retrieves all entities in the health_analysis table
@health_analysis_bp.route('/')
def get_all_ha():
    stmt = db.select(HealthAnalysis)
    ha = db.session.scalars(stmt) #multiple scalars
    return ha_schema.dump(ha)

#GET query, retrieves one entity in the health_analysis table based on the ha_id
@health_analysis_bp.route('/<int:ha_id>')
def get_one_health_analysis(ha_id):
    stmt = db.select(HealthAnalysis).filter_by(ha_id=ha_id)
    health_analysis = db.session.scalar(stmt) #single scalar
    if health_analysis:
        return health_analysis_schema.dump(health_analysis)
    else:
        return {'error': f'Health Analysis not found with id {ha_id}'}, 404
    
#POST query, adds a new entity to the health_analysis table
@health_analysis_bp.route('/', methods=['POST'])
def create_health_analysis():
    body_data = health_analysis_schema.load(request.get_json())
    health_analysis = HealthAnalysis(
        physical_change=body_data.get('physical_change'),
        mood_change=body_data.get('mood_change'),
    )
    db.session.add(health_analysis)
    db.session.commit()
    return health_analysis_schema.dump(health_analysis), 201

#DELETE query, deletes an entity from the health_analysis table
@health_analysis_bp.route('/<int:ha_id>', methods=['DELETE'])
def delete_one_health_analysis(ha_id):
    stmt = db.select(HealthAnalysis).filter_by(ha_id=ha_id)
    health_analysis = db.session.scalar(stmt)
    if health_analysis:
        db.session.delete(health_analysis)
        db.session.commit()
        return {'message': f'Health Analysis {health_analysis.ha_id} deleted successfully'}
    else:
        return {'error': f'Health Analysis not found with id {ha_id}'}, 404

#PUT/PATCH query, updates and entity in the health_analysis table based on ha_id
@health_analysis_bp.route('/<int:ha_id>', methods=['PUT', 'PATCH'])
def update_one_card(ha_id):
    body_data = health_analysis_schema.load(request.get_json())
    stmt = db.select(HealthAnalysis).filter_by(ha_id=ha_id)
    health_analysis = db.session.scalar(stmt)
    if health_analysis:
        health_analysis.physical_change = body_data.get('physical_change') or health_analysis.physical_change
        health_analysis.mood_change = body_data.get('mood_change') or health_analysis.mood_change
        db.session.commit()
        return health_analysis_schema.dump(health_analysis)
    else:
        return {'error': f'Health Analysis not found with id {ha_id}'}, 404
