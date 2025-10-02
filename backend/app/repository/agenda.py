from datetime import date, time
from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from app.models.agenda import Agenda
from app.schemas.agenda import AgendaCreate, AgendaUpdate

class AgendaRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def get_all(self, skip: int = 0, limit: int = 10) -> List[Agenda]:
        return self.session.query(Agenda).offset(skip).limit(limit).all()
    
    def get_by_id(self, agenda_id: int) -> Optional[Agenda]:
        return self.session.query(Agenda).filter(Agenda.IDagenda == agenda_id).first()
    
    def get_with_servicio(self, agenda_id: int) -> Optional[Agenda]:
        return self.session.query(Agenda).options(
            joinedload(Agenda.servicio)
        ).filter(Agenda.IDagenda == agenda_id).first()
    
    def create(self, agenda_data: AgendaCreate) -> Agenda:
        db_agenda = Agenda(**agenda_data.model_dump())
        self.session.add(db_agenda)
        self.session.commit()
        self.session.refresh(db_agenda)
        return db_agenda
    
    def update(self, agenda_id: int, agenda_data: AgendaUpdate) -> Optional[Agenda]:
        db_agenda = self.get_by_id(agenda_id)
        if db_agenda:
            update_data = agenda_data.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_agenda, field, value)
            self.session.commit()
            self.session.refresh(db_agenda)
        return db_agenda

    def delete(self, agenda_id: int) -> bool:
        db_agenda = self.get_by_id(agenda_id)
        if db_agenda:
            self.session.delete(db_agenda)
            self.session.commit()
            return True
        return False
    
    def get_by_servicio(self, servicio_id: int) -> List[Agenda]:
        return self.session.query(Agenda).filter(Agenda.IDservicio == servicio_id).all()
    
    def get_by_fecha(self, fecha: date) -> List[Agenda]:
        return self.session.query(Agenda).filter(Agenda.fecha == fecha).all()
    
    def get_conflictos_horarios(self, fecha: date, hora_inicio: time, hora_fin: time, agenda_id: int = None) -> List[Agenda]:
        """
        Verifica si hay conflictos de horario para una fecha y hora específicas
        """
        query = self.session.query(Agenda).filter(
            Agenda.fecha == fecha,
            (
                (Agenda.hora_inicio <= hora_inicio) & (Agenda.hora_fin > hora_inicio) |
                (Agenda.hora_inicio < hora_fin) & (Agenda.hora_fin >= hora_fin) |
                (Agenda.hora_inicio >= hora_inicio) & (Agenda.hora_fin <= hora_fin)
            )
        )
        
        if agenda_id:
            query = query.filter(Agenda.IDagenda != agenda_id)
            
        return query.all()