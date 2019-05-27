# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, Date, DateTime, Index, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, LONGTEXT, SMALLINT, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ConsImgtextConfig(Base):
    __tablename__ = 'cons_imgtext_config'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(64), index=True)
    DOCTOR_TITLE_CODE = Column(String(64), index=True)
    DOCTOR_TITLE_NAME = Column(String(64))
    PRICE = Column(DECIMAL(8, 2))
    DURATION = Column(INTEGER(11))


class ConsImgtextMsgRecord(Base):
    __tablename__ = 'cons_imgtext_msg_record'
    __table_args__ = (
        Index('index_ids', 'USER_ID', 'EMPLOYEE_ID', 'ORDER_ID'),
    )

    ID = Column(BIGINT(20), primary_key=True)
    ORDER_ID = Column(String(64), nullable=False)
    RECORD_TYPE = Column(INTEGER(2), nullable=False)
    RECORD_CONTENT = Column(String(1024))
    INPUT_DATE_TIME = Column(DateTime, nullable=False)
    RECORD_DIRECTION = Column(INTEGER(1), nullable=False)
    USER_ID = Column(BIGINT(20))
    EMPLOYEE_ID = Column(BIGINT(20))
    RECORD_SECONDS = Column(INTEGER(4))
    LOGIN_ID = Column(BIGINT(20))


class ConsImgtextOrder(Base):
    __tablename__ = 'cons_imgtext_order'
    __table_args__ = (
        Index('index_user_id_employee_id', 'USER_ID', 'EMPLOYEE_ID'),
    )

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(64))
    ORG_NAME = Column(String(64))
    DEPT_CODE = Column(String(64))
    DEPT_NAME = Column(String(64))
    DOCTOR_CODE = Column(String(64))
    DOCTOR_NAME = Column(String(64))
    ORDER_STATUS = Column(INTEGER(1), nullable=False, server_default=text("'0'"))
    DEFRAY_ID = Column(BIGINT(20))
    DEFRAY_RESULT = Column(INTEGER(1), server_default=text("'0'"))
    SATISFY_REMARK_STATUS = Column(INTEGER(1), server_default=text("'0'"))
    INPUT_DATE_TIME = Column(DateTime)
    UPDATE_DATE_TIME = Column(DateTime)
    END_TIME = Column(DateTime)
    EXPIRE_TIME = Column(DateTime)
    DOCTOR_REPLY_FLAG = Column(INTEGER(1))
    LAST_RECORD_TYPE = Column(INTEGER(2))
    LAST_RECORD_CONTENT = Column(String(1024))
    USER_ID = Column(BIGINT(20))
    EMPLOYEE_ID = Column(BIGINT(20))
    LOGIN_ID = Column(BIGINT(20))


class ConsIntroduction(Base):
    __tablename__ = 'cons_introduction'

    ID = Column(BIGINT(20), primary_key=True)
    BUSI_CODE = Column(String(16))
    ORG_CODE = Column(String(64), index=True)
    SERVICE_DESC = Column(Text)
    INFORMED_CONTENT = Column(Text)
    REMIND_DURATION = Column(INTEGER(10))
    REMIND_SWITCH = Column(TINYINT(10))
    EFFECTIVE_TIME = Column(INTEGER(11))


class ConsTelCallRecord(Base):
    __tablename__ = 'cons_tel_call_record'

    ID = Column(String(16), primary_key=True)
    ORDER_ID = Column(BIGINT(20))
    BEGIN_TIME = Column(DateTime)
    END_TIME = Column(DateTime)
    TALK_DURATION = Column(INTEGER(11))
    INPUT_DATE_TIME = Column(DateTime, nullable=False)
    CALLING_NUMBER = Column(String(32))
    CALLEE_NUMBER = Column(String(32))
    THIRD_CALL_ID = Column(String(64))
    LOGIN_ID = Column(BIGINT(20))


class ConsTelConfig(Base):
    __tablename__ = 'cons_tel_config'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(64))
    DOCTOR_TITLE_CODE = Column(String(64))
    DOCTOR_TITLE_NAME = Column(String(64))
    PRICE = Column(DECIMAL(8, 2))
    DURATION = Column(INTEGER(11))


class ConsTelMsgRecord(Base):
    __tablename__ = 'cons_tel_msg_record'

    ID = Column(BIGINT(20), primary_key=True)
    ORDER_ID = Column(String(64), nullable=False)
    RECORD_DIRECTION = Column(INTEGER(1), nullable=False)
    RECORD_TYPE = Column(INTEGER(2), nullable=False)
    RECORD_CONTENT = Column(String(1024))
    INPUT_DATE_TIME = Column(DateTime, nullable=False)
    USER_ID = Column(BIGINT(20))
    EMPLOYEE_ID = Column(BIGINT(20))
    RECORD_SECONDS = Column(INTEGER(11))
    LOGIN_ID = Column(BIGINT(20))


class ConsTelOrder(Base):
    __tablename__ = 'cons_tel_order'

    ID = Column(BIGINT(20), primary_key=True)
    MASTER_ORDER_ID = Column(BIGINT(20))
    ORG_CODE = Column(String(64))
    ORG_NAME = Column(String(64))
    DEPT_CODE = Column(String(64))
    DEPT_NAME = Column(String(64))
    DOCTOR_CODE = Column(String(64))
    DOCTOR_NAME = Column(String(64))
    ORDER_STATUS = Column(INTEGER(1), nullable=False, server_default=text("'0'"))
    DEFRAY_ID = Column(BIGINT(20))
    DEFRAY_RESULT = Column(INTEGER(1), server_default=text("'0'"))
    SATISFY_REMARK_STATUS = Column(INTEGER(1), server_default=text("'0'"))
    INPUT_DATE_TIME = Column(DateTime)
    UPDATE_DATE_TIME = Column(DateTime)
    END_TIME = Column(DateTime)
    VALID_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    APPOINTMENT_DATE = Column(Date)
    APPOINTMENT_START_TIME = Column(String(8))
    APPOINTMENT_TIME_PERIOD = Column(String(11))
    MOBILE_NUMBER = Column(String(11))
    WORKSHIFT_ID = Column(BIGINT(20))
    USER_ID = Column(BIGINT(20))
    EMPLOYEE_ID = Column(BIGINT(20))
    LOGIN_ID = Column(BIGINT(20))


class ConsVideoConfig(Base):
    __tablename__ = 'cons_video_config'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(64))
    DOCTOR_TITLE_CODE = Column(String(64))
    DOCTOR_TITLE_NAME = Column(String(64))
    PRICE = Column(DECIMAL(8, 2))
    DURATION = Column(INTEGER(11))


class ConsVideoMsgRecord(Base):
    __tablename__ = 'cons_video_msg_record'

    ID = Column(BIGINT(20), primary_key=True)
    ORDER_ID = Column(BIGINT(20), nullable=False)
    RECORD_DIRECTION = Column(INTEGER(1), nullable=False)
    RECORD_TYPE = Column(INTEGER(2), nullable=False)
    RECORD_CONTENT = Column(String(1024))
    INPUT_DATE_TIME = Column(DateTime, nullable=False)
    USER_ID = Column(BIGINT(20))
    EMPLOYEE_ID = Column(BIGINT(20))
    RECORD_SECONDS = Column(INTEGER(11))
    LOGIN_ID = Column(BIGINT(20))


class ConsVideoOrder(Base):
    __tablename__ = 'cons_video_order'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(64))
    ORG_NAME = Column(String(64))
    DEPT_CODE = Column(String(64))
    DEPT_NAME = Column(String(64))
    DOCTOR_CODE = Column(String(64))
    DOCTOR_NAME = Column(String(64))
    EMPLOYEE_ID = Column(BIGINT(20))
    ORDER_STATUS = Column(INTEGER(1), nullable=False, server_default=text("'0'"))
    DEFRAY_ID = Column(BIGINT(20))
    DEFRAY_RESULT = Column(INTEGER(1), server_default=text("'0'"))
    EXPIRED_DATE_TIME = Column(DateTime)
    SATISFY_REMARK_STATUS = Column(INTEGER(1), server_default=text("'0'"))
    INPUT_DATE_TIME = Column(DateTime)
    UPDATE_DATE_TIME = Column(DateTime)
    END_TIME = Column(DateTime)
    APPOINTMENT_DATE = Column(Date)
    APPOINTMENT_START_TIME = Column(String(8))
    APPOINTMENT_TIME_PERIOD = Column(String(11))
    BUSI_WORKSHIFT_ID = Column(BIGINT(20))
    WORKSHIFT_SERIES_NUM = Column(INTEGER(11))
    USER_ID = Column(BIGINT(20))
    ROOM_NO = Column(String(64))
    CALL_FLAG = Column(INTEGER(2), server_default=text("'0'"))
    LOGIN_ID = Column(BIGINT(20))


class ConsVideoRecord(Base):
    __tablename__ = 'cons_video_record'

    VIDEO_ID = Column(BIGINT(20), primary_key=True)
    CREATER_DATE = Column(Date, nullable=False)
    START_TIME = Column(DateTime, nullable=False)
    END_TIME = Column(DateTime, nullable=False)
    LENGTH_TIME = Column(INTEGER(11))
    OGR_CODE = Column(String(64))
    DEPT_CODE = Column(String(64))
    ORDER_ID = Column(BIGINT(20), nullable=False)
    ROOM_NO = Column(String(64))
    STAFF_NAME = Column(String(64))
    STAFF_CODE = Column(String(64))
    ID_TYPE = Column(INTEGER(11))
    ID_NO = Column(String(64))
    PATIENT_NAME = Column(String(64))
    PATIENT_AGE = Column(INTEGER(11))
    PATIENT_SEX = Column(INTEGER(11))


class CrdExam(Base):
    __tablename__ = 'crd_exam'

    ID = Column(BIGINT(20), primary_key=True)
    VISIT_ID = Column(BIGINT(20), nullable=False)
    SERIAL_NO = Column(String(32), nullable=False)
    ORG_CODE = Column(String(32), nullable=False)
    ORG_NAME = Column(String(32))
    ID_TYPE = Column(INTEGER(3), server_default=text("'1'"))
    ID_NO = Column(String(32))
    STATUS = Column(INTEGER(1), nullable=False, server_default=text("'3'"))
    ITEM_CODE = Column(String(32))
    ITEM_NAME = Column(String(64))
    PART = Column(String(32))
    PARAMETER = Column(String(32))
    REQUEST_DATE_TIME = Column(DateTime)
    FINISHED_DATE_TIME = Column(DateTime)
    UPLOAD_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    DEL_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    INPUT_DATE_TIME = Column(DateTime)
    UPDATE_DATE_TIME = Column(DateTime)
    CHARGE_FLAG = Column(INTEGER(1))


class CrdLabTest(Base):
    __tablename__ = 'crd_lab_test'

    ID = Column(BIGINT(20), primary_key=True)
    VISIT_ID = Column(BIGINT(20), nullable=False)
    SERIAL_NO = Column(String(32), nullable=False)
    ORG_CODE = Column(String(32), nullable=False)
    ORG_NAME = Column(String(32))
    ID_TYPE = Column(INTEGER(3), server_default=text("'1'"))
    ID_NO = Column(String(32))
    STATUS = Column(INTEGER(1), nullable=False, server_default=text("'3'"))
    ITEM_CODE = Column(String(32))
    ITEM_NAME = Column(String(32))
    REQUEST_DATE_TIME = Column(DateTime)
    FINISHED_DATE_TIME = Column(DateTime)
    UPLOAD_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    DEL_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    INPUT_DATE_TIME = Column(DateTime)
    UPDATE_DATE_TIME = Column(DateTime, nullable=False)
    CHARGE_FLAG = Column(INTEGER(1))


class CrdPresc(Base):
    __tablename__ = 'crd_presc'

    ID = Column(BIGINT(20), primary_key=True)
    VISIT_ID = Column(BIGINT(20), nullable=False)
    SERIAL_NO = Column(String(32), nullable=False)
    ORG_CODE = Column(String(32), nullable=False)
    ORG_NAME = Column(String(32))
    ID_TYPE = Column(INTEGER(3), server_default=text("'1'"))
    ID_NO = Column(String(32))
    PRESC_DATE_TIME = Column(DateTime)
    DEPT_CODE = Column(String(32))
    DEPT_NAME = Column(String(32))
    DOCTOR_NAME = Column(String(32))
    DOCTOR_CODE = Column(String(32))
    TOTAL_AMOUNT = Column(DECIMAL(12, 2))
    CHARGE_FLAG = Column(INTEGER(1))
    PRESC_TYPE = Column(INTEGER(3))
    DRUGS_COUNT = Column(INTEGER(3))
    INFUSION_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    ANTIBIOTICS_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    AMOUNT_BASIC_DRUG = Column(INTEGER(3))
    BASIC_DRUG_COST = Column(DECIMAL(12, 2))
    SUPPLEMENT_DRUG_COST = Column(DECIMAL(12, 2))
    AMOUNT_SUPPLEMENT_DRUG = Column(INTEGER(3))
    AMOUNT_OTHER_DRUG = Column(INTEGER(3))
    UPLOAD_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    DEL_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    INPUT_DATE_TIME = Column(DateTime, nullable=False)
    UPDATE_DATE_TIME = Column(DateTime, nullable=False)


class CrdVisit(Base):
    __tablename__ = 'crd_visit'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(32), nullable=False)
    ORG_NAME = Column(String(32))
    ID_TYPE = Column(INTEGER(3), server_default=text("'1'"))
    ID_NO = Column(String(32))
    HIS_VISIT_NO = Column(String(16))
    VISIT_TYPE = Column(INTEGER(3), nullable=False)
    REVISIT_FLAG = Column(INTEGER(1))
    NAME = Column(String(32))
    SEX = Column(INTEGER(1))
    VISIT_START_DATE_TIME = Column(DateTime, nullable=False)
    VISIT_END_DATE_TIME = Column(DateTime)
    VISIT_DESCRIPTION = Column(String(64))
    DIAGNOSE = Column(String(64))
    SUBJECTIVE = Column(String(500))
    GB_DEPT_CODE = Column(String(32))
    HIS_DEPT_CODE = Column(String(32))
    HIS_DEPT_NAME = Column(String(32))
    INSURANCE_TYPE = Column(INTEGER(3), nullable=False, server_default=text("'9'"))
    PAY_TYPE = Column(INTEGER(3), nullable=False, server_default=text("'1'"))
    DOCTOR_CODE = Column(String(32))
    DOCTOR_NAME = Column(String(32))
    UPLOAD_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    DEL_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    INPUT_DATE_TIME = Column(DateTime, nullable=False)
    UPDATE_DATE_TIME = Column(DateTime)
    SOURCE_FLAG = Column(INTEGER(3))


class DoDoctorOrderTemplate(Base):
    __tablename__ = 'do_doctor_order_template'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(64))
    DEPT_CODE = Column(String(64))
    DOCTOR_ID = Column(BIGINT(20))
    DOCTOR_CODE = Column(String(64))
    TEMPLATE_NAME = Column(String(64))
    TEMPLATE_TYPE = Column(INTEGER(2))
    TEMPLATE_INFO = Column(Text)
    CREATE_TIME = Column(DateTime)
    UPDATE_TIME = Column(DateTime)
    VISIBLE_RANGE = Column(INTEGER(4), server_default=text("'0'"))
    CATEGORY = Column(INTEGER(2))


class EprAddres(Base):
    __tablename__ = 'epr_address'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(64))
    ORG_NAME = Column(String(64))
    MEDI_ROOM_TYPE = Column(String(64))
    MEDI_ROOM_NAME = Column(String(64))
    MEDI_ROOM_ADDRESS = Column(String(512))
    MEDI_ROOM_TEL = Column(String(32))
    MEMO = Column(String(256))
    LONGITUDE = Column(String(64))
    LATITUDE = Column(String(64))
    CREATE_TIME = Column(DateTime)
    CREATOR = Column(String(32))
    MODIFY_TIME = Column(DateTime)
    MODIFIER = Column(String(32))


class EprAddressRelationship(Base):
    __tablename__ = 'epr_address_relationship'

    ID = Column(BIGINT(20), primary_key=True)
    PRESC_ID = Column(BIGINT(20), unique=True)
    MEDI_ADDRESS_ID = Column(BIGINT(20))


class EprConfig(Base):
    __tablename__ = 'epr_config'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(32))
    ORG_NAME = Column(String(32))
    IF_SELF_GET = Column(TINYINT(4))
    IF_SELF_ORG_SEND = Column(TINYINT(4))
    IF_AROUND_MED = Column(TINYINT(4))
    IF_ONLINE_MED = Column(TINYINT(4))
    CREATE_TIME = Column(DateTime)
    UPDATE_TIME = Column(DateTime)
    CREATER = Column(String(10))
    UPDATER = Column(String(10))


class EprMedicine(Base):
    __tablename__ = 'epr_medicine'

    ID = Column(BIGINT(18), primary_key=True)
    PRESC_ID = Column(BIGINT(20))
    MEDI_CODE = Column(String(16))
    MEDI_NAME = Column(String(32))
    MEDI_PRICE = Column(DECIMAL(12, 2))
    SPECIFICATION = Column(String(128))
    AMOUNT = Column(INTEGER(11))
    FREQUENCY = Column(String(64))
    FREQUENCY_CODE = Column(String(64))
    FREQUENCY_NAME = Column(String(64))
    DOSE = Column(String(64))
    DOSE_UNIT = Column(String(64))
    MEDI_USAGE = Column(String(64))
    USAGE_MEMO = Column(String(512))
    PACKAGE_CONTENT = Column(INTEGER(10))
    PACKAGE_UNIT = Column(String(64))
    UNITS = Column(String(128))
    SOCIAL_DIR_CLASS = Column(INTEGER(1))
    SOCIAL_DIR_CODE = Column(String(16))
    HOSPITAL_DIR_CODE = Column(String(16))
    HOSPITAL_DIR_NAME = Column(String(32))
    BILL_CLASS = Column(INTEGER(1))


class EprOrder(Base):
    __tablename__ = 'epr_order'

    ID = Column(BIGINT(20), primary_key=True)
    PRESC_ID = Column(BIGINT(20))
    ORG_CODE = Column(String(64))
    ORG_NAME = Column(String(64))
    DEPT_CODE = Column(String(64))
    DEPT_NAME = Column(String(64))
    DOCTOR_CODE = Column(String(64))
    DOCTOR_NAME = Column(String(64))
    MEDI_TAKE_TYPE = Column(INTEGER(1), server_default=text("'1'"))
    ORDER_STATUS = Column(INTEGER(1), nullable=False, server_default=text("'0'"))
    DEFRAY_ID = Column(BIGINT(20))
    DEFRAY_RESULT = Column(INTEGER(1), server_default=text("'0'"))
    INPUT_DATE_TIME = Column(DateTime)
    UPDATE_DATE_TIME = Column(DateTime)
    UPDATE_MEMO = Column(Text)


class EprPharmacyRecord(Base):
    __tablename__ = 'epr_pharmacy_record'

    ID = Column(BIGINT(20), primary_key=True)
    PRESC_ID = Column(BIGINT(20))
    PHARMACY_ID = Column(BIGINT(20))
    INPUT_DATE_TIME = Column(DateTime)
    UPDATE_DATE_TIME = Column(DateTime)
    LAST_MODIFIER = Column(String(32))
    AUDITOR = Column(String(32))
    PHARMACIST = Column(String(32))
    STATUS = Column(INTEGER(3), server_default=text("'1'"))
    REJECT_REASON = Column(String(512))


class EprRecord(Base):
    __tablename__ = 'epr_record'

    ID = Column(BIGINT(20), primary_key=True)
    VISIT_ID = Column(BIGINT(20))
    REGISTER_ID = Column(BIGINT(20))
    BUSI_TYPE = Column(INTEGER(3))
    USER_ID = Column(BIGINT(20), nullable=False)
    ORG_CODE = Column(String(32), nullable=False)
    ORG_NAME = Column(String(32))
    PRESC_DATE_TIME = Column(DateTime)
    DEPT_CODE = Column(String(32))
    DEPT_NAME = Column(String(32))
    DOCTOR_NAME = Column(String(32))
    DOCTOR_CODE = Column(String(32))
    COST_CLASS = Column(INTEGER(1))
    PHARMACIST = Column(String(32))
    SUBJECTIVE = Column(String(256))
    ICD10_CODE = Column(String(256))
    DIAGNOSE = Column(String(256))
    TOTAL_AMOUNT = Column(DECIMAL(12, 2))
    CHARGE_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    MEDI_TAKE_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    PRESC_TYPE = Column(INTEGER(3))
    EXPIRE_TIME = Column(DateTime)
    DRUGS_COUNT = Column(INTEGER(3))
    INFUSION_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    ANTIBIOTICS_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    AMOUNT_BASIC_DRUG = Column(INTEGER(3))
    BASIC_DRUG_COST = Column(DECIMAL(12, 2))
    SUPPLEMENT_DRUG_COST = Column(DECIMAL(12, 2))
    AMOUNT_SUPPLEMENT_DRUG = Column(INTEGER(3))
    AMOUNT_OTHER_DRUG = Column(INTEGER(3))
    INPUT_DATE_TIME = Column(DateTime)
    UPDATE_DATE_TIME = Column(DateTime)
    FROM_TYPE = Column(INTEGER(2))
    MOBILE_NUMBER = Column(String(20))
    INSURANCE_CARD_NO = Column(String(100))
    CARD_TYPE = Column(String(64))
    IS_YELLOW_CARD = Column(String(8))
    FEE_TYPE = Column(String(64))
    PAY_ENTITY = Column(String(512))
    SIGN_CONTENT = Column(String(512))
    EPR_STATUS = Column(INTEGER(11), server_default=text("'0'"))
    LAST_PHARMACY_RECORD_ID = Column(BIGINT(20))


class EprTempMedicine(Base):
    __tablename__ = 'epr_temp_medicine'

    id = Column(BIGINT(20), primary_key=True)
    ysgh = Column(String(100))
    ysmc = Column(String(100))
    zdmc = Column(String(255))
    kdsj = Column(String(100))
    cfsb = Column(String(100))
    jzkh = Column(String(100))
    xh = Column(String(100))
    ypxh = Column(String(100))
    ypmc = Column(String(100))
    gg = Column(String(100))
    dj = Column(String(100))
    gyfs = Column(String(100))
    pl = Column(String(100))
    ycjl = Column(String(100))
    jldw = Column(String(100))
    sl = Column(String(100))
    dw = Column(String(100))


class FbEventOperate(Base):
    __tablename__ = 'fb_event_operate'

    ID = Column(BIGINT(18), primary_key=True)
    EVENT_ID = Column(BIGINT(20), nullable=False)
    STATUS = Column(INTEGER(1), nullable=False)
    PROCESSOR_CODE = Column(String(32))
    PROCESSOR_NAME = Column(String(32))
    PROCESS_TIME = Column(DateTime, nullable=False)


class FbManualCheck(Base):
    __tablename__ = 'fb_manual_check'

    ID = Column(BIGINT(20), primary_key=True)
    CSRP_ID = Column(BIGINT(20))
    REFLECT_PURPOSE = Column(INTEGER(1))
    CONTENT_CATEGORY = Column(INTEGER(1))
    PROCESSOR_CODE = Column(String(32))
    PROCESSOR_NAME = Column(String(32))
    STATUS = Column(INTEGER(1))
    RESULT = Column(INTEGER(1))
    SUGGESTION = Column(String(128))
    CHECK_TIME = Column(DateTime)


class FbQuesAttachment(Base):
    __tablename__ = 'fb_ques_attachment'

    ID = Column(BIGINT(20), primary_key=True)
    FB_ID = Column(BIGINT(20))
    LINK_URL = Column(String(256))
    LINK_DESC = Column(String(128))
    LINK_FILE_TYPE = Column(String(8))


class FbQuesRecord(Base):
    __tablename__ = 'fb_ques_record'

    ID = Column(BIGINT(20), primary_key=True)
    USER_ID = Column(BIGINT(20))
    APP_UNIQUE_ID = Column(String(64))
    CONTENT = Column(Text)
    FD_TIME = Column(DateTime)
    SOURCE_TYPE = Column(INTEGER(1))


class FdEventProces(Base):
    __tablename__ = 'fd_event_process'

    EVENT_ID = Column(BIGINT(20), primary_key=True)
    CSRP_ID = Column(BIGINT(20), nullable=False)
    ____ID = Column('????ID', BIGINT(20))
    STATUS = Column(INTEGER(1))
    PROCESS_INFO = Column(String(256))
    PROCESS_SUGGESTION = Column(String(256))
    REVIEW_FLAG = Column(INTEGER(1))
    REVIEW_INFO = Column(String(256))


class MdMedicine(Base):
    __tablename__ = 'md_medicine'
    __table_args__ = (
        Index('medicine_unique', 'MEDI_CODE', 'ORG_CODE', unique=True),
    )

    ID = Column(BIGINT(18), primary_key=True)
    DISEASE_ID = Column(BIGINT(20))
    MEDI_CODE = Column(String(16))
    MEDI_NAME = Column(String(64))
    LOGOGRAM = Column(String(64))
    MEDI_PRICE = Column(DECIMAL(12, 2))
    UNITS = Column(String(128))
    THUMBNAIL = Column(String(128))
    ORIGINAL = Column(String(128))
    STATE = Column(String(1), server_default=text("'1'"))
    BILL_CLASS = Column(String(3))
    SPECIFICATION = Column(String(32))
    MEDI_TYPE = Column(INTEGER(3))
    DOSE = Column(INTEGER(8))
    DOSE_UNIT = Column(String(32))
    MEDI_USAGE_NO = Column(String(32))
    MEDI_USAGE = Column(String(64))
    FREQUENCY_CODE = Column(String(32))
    FREQUENCY = Column(INTEGER(8))
    FREQUENCY_NAME = Column(String(32))
    PACKAGE_UNIT = Column(String(32))
    PRODUCTION_NO = Column(String(32))
    PRODUCTION_ADDRESS = Column(String(256))
    DEFAULT_DAYS = Column(INTEGER(4))
    PACKAGE_CONTENT = Column(INTEGER(10))
    ORG_CODE = Column(String(64))
    CATEGORY = Column(INTEGER(2))


class MdMedicineStock(Base):
    __tablename__ = 'md_medicine_stock'
    __table_args__ = (
        Index('medicine_unique', 'MEDI_CODE', 'ORG_CODE', unique=True),
    )

    ID = Column(BIGINT(20), primary_key=True)
    MEDI_ID = Column(BIGINT(20))
    STOCK = Column(INTEGER(11))
    MEDI_CODE = Column(String(16))
    MEDI_COST_PRICE = Column(DECIMAL(12, 2))
    MEDI_PRICE = Column(DECIMAL(12, 2))
    ORG_CODE = Column(String(64))
    CREATE_TIME = Column(DateTime)
    UPDATE_TIME = Column(DateTime)


class MedEleRecipeManage(Base):
    __tablename__ = 'med_ele_recipe_manage'

    id = Column(BIGINT(20), primary_key=True)
    org_code = Column(String(32), index=True)
    org_name = Column(String(100))
    if_self_get = Column(TINYINT(4))
    if_self_org_send = Column(TINYINT(4))
    if_around_med = Column(TINYINT(4))
    if_online_med = Column(TINYINT(4))
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    creater = Column(BIGINT(10))
    updater = Column(BIGINT(10))


class MedHospitalMedManage(Base):
    __tablename__ = 'med_hospital_med_manage'

    id = Column(BIGINT(20), primary_key=True)
    org_code = Column(String(50), index=True)
    org_name = Column(String(100))
    med_name = Column(String(50))
    med_type = Column(String(20))
    med_address = Column(String(300))
    med_phone = Column(String(11))
    create_time = Column(DateTime)
    creater = Column(BIGINT(10))
    update_time = Column(DateTime)
    updater = Column(BIGINT(10))


class MsgMessageRecord(Base):
    __tablename__ = 'msg_message_record'
    __table_args__ = (
        Index('Index_1', 'REV_USER_TYPE', 'REV_USER_ID', 'MESSAGE_TYPE', unique=True),
    )

    ID = Column(BIGINT(20), primary_key=True)
    REV_USER_TYPE = Column(INTEGER(1), nullable=False)
    REV_USER_ID = Column(BIGINT(20), nullable=False)
    MESSAGE_TYPE = Column(INTEGER(2), nullable=False)
    MESSAGE_CONTENT = Column(String(512))
    UNREAD_COUNT = Column(INTEGER(11))
    INPUT_TIME = Column(DateTime, nullable=False)
    UPDATE_TIME = Column(DateTime)


class MsgPushMessage(Base):
    __tablename__ = 'msg_push_message'
    __table_args__ = (
        Index('index_login_id', 'LOGIN_ID', 'USER_ID'),
    )

    ID = Column(BIGINT(20), primary_key=True)
    LOGIN_ID = Column(BIGINT(20))
    USER_ID = Column(BIGINT(20))
    MESSAGE_TYPE = Column(INTEGER(2))
    MESSAGE_INFO = Column(String(1024))
    CREATE_TIME = Column(DateTime)


class MsgPushMessageHistory(Base):
    __tablename__ = 'msg_push_message_history'
    __table_args__ = (
        Index('index_loginID', 'LOGIN_ID', 'USER_ID'),
    )

    ID = Column(BIGINT(20), primary_key=True)
    LOGIN_ID = Column(BIGINT(20))
    USER_ID = Column(BIGINT(20))
    MESSAGE_TYPE = Column(INTEGER(2))
    MESSAGE_INFO = Column(String(1024))
    CREATE_TIME = Column(DateTime)


class MsgRemindRecordDetail(Base):
    __tablename__ = 'msg_remind_record_detail'
    __table_args__ = (
        Index('Index_1', 'REV_USER_TYPE', 'REV_USER_ID', 'MESSAGE_TYPE', 'SEND_TIME', unique=True),
    )

    ID = Column(BIGINT(20), primary_key=True)
    REV_USER_TYPE = Column(INTEGER(1), nullable=False)
    REV_USER_ID = Column(BIGINT(20), nullable=False)
    MESSAGE_TYPE = Column(INTEGER(2), nullable=False)
    MESSAGE_CONTENT = Column(String(1024), nullable=False)
    SEND_TIME = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    SOURCE_TYPE = Column(INTEGER(1))
    ORG_CODE = Column(String(64))
    ORG_NAME = Column(String(64))
    INPUT_TIME = Column(DateTime, nullable=False)
    EMPLOYEE_ID = Column(BIGINT(20))
    BUSI_ORDER_ID = Column(BIGINT(20))


class NcdDiseaseConfig(Base):
    __tablename__ = 'ncd_disease_config'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(64))
    DOCTOR_TITLE_CODE = Column(String(64))
    DOCTOR_TITLE_NAME = Column(String(64))
    PRICE = Column(DECIMAL(8, 2))
    DURATION = Column(INTEGER(11))


class NcdLastRecord(Base):
    __tablename__ = 'ncd_last_record'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(64), nullable=False)
    USER_ID = Column(BIGINT(20), nullable=False)
    CATEGORY_ID = Column(BIGINT(20), nullable=False)
    NCD_REGISTER_ID = Column(BIGINT(20))


class NcdMsgRecord(Base):
    __tablename__ = 'ncd_msg_record'

    ID = Column(BIGINT(20), primary_key=True)
    ORDER_ID = Column(BIGINT(20), nullable=False)
    RECORD_DIRECTION = Column(INTEGER(1), nullable=False)
    RECORD_TYPE = Column(INTEGER(2), nullable=False)
    RECORD_CONTENT = Column(String(1024))
    INPUT_DATE_TIME = Column(DateTime, nullable=False)
    USER_ID = Column(BIGINT(20))
    EMPLOYEE_ID = Column(BIGINT(20))
    RECORD_SECONDS = Column(INTEGER(11))


class NcdRegister(Base):
    __tablename__ = 'ncd_register'
    __table_args__ = (
        Index('index_userId', 'USER_ID', 'LOGIN_ID', 'EMPLOYEE_ID'),
    )

    ID = Column(BIGINT(20), primary_key=True)
    MASTER_ORDER_ID = Column(BIGINT(20))
    USER_ID = Column(BIGINT(20), nullable=False)
    LOGIN_ID = Column(BIGINT(20), nullable=False)
    ORG_CODE = Column(String(64))
    ORG_NAME = Column(String(64))
    DEPT_CODE = Column(String(64))
    DEPT_NAME = Column(String(64))
    EMPLOYEE_ID = Column(BIGINT(20))
    DOCTOR_CODE = Column(String(64))
    DOCTOR_NAME = Column(String(64))
    HISTORY_PRESC_ID = Column(BIGINT(20))
    ORDER_STATUS = Column(INTEGER(1), nullable=False, server_default=text("'0'"))
    DEFRAY_ID = Column(BIGINT(20))
    DEFRAY_RESULT = Column(INTEGER(1), server_default=text("'0'"))
    SATISFY_REMARK_STATUS = Column(INTEGER(1), server_default=text("'0'"))
    UPDATE_DATE_TIME = Column(DateTime)
    END_TIME = Column(DateTime)
    APPOINTMENT_DATE = Column(Date)
    APPOINTMENT_START_TIME = Column(String(8))
    APPOINTMENT_TIME_PERIOD = Column(String(11))
    MOBILE_NUMBER = Column(String(11))
    TEL_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    BUSI_WORKSHIFT_ID = Column(BIGINT(20))
    WORKSHIFT_SERIES_NUM = Column(INTEGER(11))
    ROOM_NO = Column(String(64))
    CALL_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    DISEASE_IDS = Column(String(64))
    DISEASE_NAMES = Column(String(300))
    CREATE_DATE_TIME = Column(DateTime)
    FROM_TYPE = Column(INTEGER(2))
    SORT_NO = Column(INTEGER(4))
    VISIT_DATE_TIME = Column(DateTime)


class NcdTelCallRecord(Base):
    __tablename__ = 'ncd_tel_call_record'

    ID = Column(String(16), primary_key=True)
    ORDER_ID = Column(BIGINT(20))
    BEGIN_TIME = Column(DateTime)
    END_TIME = Column(DateTime)
    TALK_DURATION = Column(INTEGER(11))
    INPUT_DATE_TIME = Column(DateTime, nullable=False)
    CALLING_NUMBER = Column(String(32))
    CALLEE_NUMBER = Column(String(32))
    THIRD_CALL_ID = Column(String(64))
    RECORD_URL = Column(String(1024))


class NcdVideoRecord(Base):
    __tablename__ = 'ncd_video_record'

    VIDEO_ID = Column(BIGINT(20), primary_key=True)
    CREATER_DATE = Column(Date, nullable=False)
    START_TIME = Column(DateTime, nullable=False)
    END_TIME = Column(DateTime, nullable=False)
    LENGTH_TIME = Column(INTEGER(11))
    OGR_CODE = Column(String(64))
    DEPT_CODE = Column(String(64))
    ORDER_ID = Column(BIGINT(20), nullable=False)
    ROOM_NO = Column(String(64))
    STAFF_NAME = Column(String(64))
    STAFF_CODE = Column(String(64))
    ID_TYPE = Column(INTEGER(11))
    ID_NO = Column(String(64))
    PATIENT_NAME = Column(String(64))
    PATIENT_AGE = Column(INTEGER(11))
    PATIENT_SEX = Column(INTEGER(11))


class OrdDelevery(Base):
    __tablename__ = 'ord_delevery'

    ID = Column(BIGINT(20), primary_key=True)
    ORDER_ID = Column(BIGINT(20))
    LOGISTIC_COMP_CODE = Column(String(64))
    LOGISTIC_COMP_NAME = Column(String(64))
    TRACKING_NUMBER = Column(String(64))
    LOGISTIC_STATE_CODE = Column(String(3))
    LOGISTIC_STATE_DESC = Column(String(64))
    CREATE_TIME = Column(DateTime)
    MODIFY_TIME = Column(DateTime)


class OrdRecord(Base):
    __tablename__ = 'ord_record'

    ORDER_ID = Column(BIGINT(18), primary_key=True)
    ORDER_NAME = Column(String(32))
    USER_ID = Column(BIGINT(20))
    BUSI_ORDER_TYPE = Column(INTEGER(2))
    BUSI_ORDER_ID = Column(BIGINT(20))
    ORG_CODE = Column(String(32))
    ORG_NAME = Column(String(32))
    PATIENT_NAME = Column(String(32))
    DOCTOR_NAME = Column(String(32))
    MEDI_TAKE_TYPE = Column(INTEGER(1), server_default=text("'1'"))
    APP_ID = Column(String(32))
    APP_TYPE = Column(INTEGER(3))
    ORDER_START_TIME = Column(DateTime)
    EXPIRE_TIME = Column(DateTime)
    TOTAL_AMOUNT = Column(DECIMAL(8, 2))
    PAY_AMOUNT = Column(DECIMAL(8, 2))
    MEDI_INSU_AMOUNT = Column(DECIMAL(8, 2))
    DELIVERY_AMOUNT = Column(DECIMAL(8, 2))
    ADDRESS_ID = Column(BIGINT(20))
    DEFRAY_RESULT = Column(INTEGER(1), server_default=text("'0'"))
    INPUT_DATE_TIME = Column(DateTime)
    UPDATE_DATE_TIME = Column(DateTime)
    CANCEL_CAUSE = Column(String(128))
    CANCEL_TIME = Column(DateTime)
    CANCEL_TYPE = Column(INTEGER(1), server_default=text("'0'"))


class OrdTransaction(Base):
    __tablename__ = 'ord_transaction'

    ID = Column(BIGINT(18), primary_key=True)
    ORDER_ID = Column(BIGINT(18), nullable=False)
    DIRECTION = Column(INTEGER(1))
    PAYMENT_DATE_TIME = Column(DateTime)
    PRODUCT_TYPE = Column(String(16))
    PAYMENT_ACCOUNT_NO = Column(String(32))
    PAYMENT_NO = Column(String(32))
    PAYMENT_FEE = Column(DECIMAL(12, 2))
    DEFRAY_ID = Column(BIGINT(20))
    INPUT_DATE_TIME = Column(DateTime)
    UPDATE_DATE_TIME = Column(DateTime)


class PBusiClas(Base):
    __tablename__ = 'p_busi_class'

    ID = Column(BIGINT(20), primary_key=True)
    BUSI_CODE = Column(String(16))
    BUSI_DESC = Column(String(64))


class PCategory2Disease(Base):
    __tablename__ = 'p_category_2_disease'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(64))
    CATEGORY_ID = Column(BIGINT(20))
    DISEASE_ID = Column(BIGINT(20))


class PDiseaseCategory(Base):
    __tablename__ = 'p_disease_category'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(64))
    DISEASE_NAME = Column(String(128))
    ICD10_CODE = Column(String(64))
    DISEASE_DESCRIPTION = Column(String(512))
    DISEASE_TYPE = Column(INTEGER(3))
    INVALID_FLAG = Column(INTEGER(1))
    CREATER_ID = Column(BIGINT(20))
    CREATE_TIME = Column(DateTime)
    MODIFIER_ID = Column(BIGINT(20))
    MODIFY_TIME = Column(DateTime)


class PDiseaseInfo(Base):
    __tablename__ = 'p_disease_info'
    __table_args__ = (
        Index('UNIQUE KEY', 'ICD10_CODE', 'DISEASE_NAME', unique=True),
    )

    ID = Column(BIGINT(20), primary_key=True)
    CATEGORY_ID = Column(BIGINT(20))
    ICD10_CODE = Column(String(64))
    DISEASE_NAME = Column(String(128))
    LOGOGRAM = Column(String(128))
    DISEASE_DESCRIPTION = Column(String(512))
    INVALID_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    CREATER_ID = Column(BIGINT(20))
    CREATE_TIME = Column(DateTime)
    MODIFIER_ID = Column(BIGINT(20))
    MODIFY_TIME = Column(DateTime)


class PDoctor2Busiclas(Base):
    __tablename__ = 'p_doctor_2_busiclass'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(64))
    EMPLOYEE_ID = Column(BIGINT(20), index=True)
    BUSI_CODE = Column(String(16))


class PDoctor2Disease(Base):
    __tablename__ = 'p_doctor_2_disease'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(64))
    EMPLOYEE_ID = Column(BIGINT(20))
    DISEASE_ID = Column(BIGINT(20))


class PDoctorEcard(Base):
    __tablename__ = 'p_doctor_ecard'
    __table_args__ = (
        Index('doctor_index', 'ORG_CODE', 'EMPLOYEE_ID', 'BUSI_CODE', unique=True),
    )

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(64))
    EMPLOYEE_ID = Column(BIGINT(20))
    VISIT_NUMBER = Column(INTEGER(11))
    REMARK_NUMBER = Column(INTEGER(11))
    PRAISE_NUMBER = Column(INTEGER(11))
    TOTAL_SCORE = Column(INTEGER(11))
    BUSI_CODE = Column(String(16))


class PDoctorWorkshfitSee(Base):
    __tablename__ = 'p_doctor_workshfit_see'

    ID = Column(BIGINT(20), primary_key=True)
    EMPLOYEE_ID = Column(BIGINT(20), nullable=False)
    WORKSHIFT_ID = Column(BIGINT(20), nullable=False)
    NOW_SERIES_NUM = Column(String(16), nullable=False)
    OPERATION_TIME = Column(DateTime, nullable=False)


class PEmp2Org(Base):
    __tablename__ = 'p_emp_2_org'
    __table_args__ = (
        Index('index_mix', 'DEPT_ID', 'ORG_ID', 'ORG_CODE', 'DEPT_CODE'),
    )

    ID = Column(BIGINT(20), primary_key=True)
    EMPLOYEE_ID = Column(BIGINT(20))
    ORG_ID = Column(BIGINT(20), nullable=False)
    ORG_CODE = Column(String(64), nullable=False)
    DEPT_ID = Column(BIGINT(20))
    DEPT_CODE = Column(String(64))
    EMPLOYEE_CODE = Column(String(32))
    HIS_EMPLOYEE_CODE = Column(String(64))
    DEFAULT_FLAG = Column(INTEGER(1))


class PEmployee(Base):
    __tablename__ = 'p_employee'

    ID = Column(BIGINT(20), primary_key=True, unique=True)
    EMPLOYEE_NAME = Column(String(32))
    ID_TYPE = Column(INTEGER(3), nullable=False)
    ID_NO = Column(String(32))
    SEX = Column(String(1))
    DATE_OF_BIRTH = Column(DateTime)
    PASSWORD = Column(String(128))
    JOB = Column(String(16))
    TITLE_CODE = Column(String(16))
    TITLE_NAME = Column(String(22))
    EDUCATION = Column(String(16))
    REGULAR_STATUS = Column(INTEGER(1))
    EMPLOYEE_TYPE = Column(INTEGER(1))
    PHOTO_URL = Column(String(256))
    MOBILE_NUMBER = Column(String(20))
    WEIBO = Column(String(32))
    WEIXIN = Column(String(32))
    DESCRIPTION = Column(String(256))
    GOODAT = Column(String(256))
    STATUS = Column(INTEGER(1), nullable=False)
    CERTIFICATION_NUMBER = Column(String(50))
    BUSINESS_REGION = Column(String(100))
    SIGN_URL = Column(String(256))


class PLoginAccount(Base):
    __tablename__ = 'p_login_account'

    ID = Column(BIGINT(20), primary_key=True)
    EMPLOYEE_ID = Column(BIGINT(20), nullable=False)
    TYPE = Column(INTEGER(11), nullable=False)
    LOGIN_ACCOUNT = Column(String(64), nullable=False)


class PLoginTraceInfo(Base):
    __tablename__ = 'p_login_trace_info'

    ID = Column(BIGINT(20), primary_key=True)
    EMPLOYEE_ID = Column(BIGINT(20), nullable=False)
    ACCOUNT_TYPE = Column(INTEGER(11))
    ACCOUNT_NO = Column(String(64))
    LOGIN_TIME = Column(DateTime)
    LOGOUT_TIME = Column(DateTime)
    SYS_CODE = Column(String(16))
    ORG_CODE = Column(String(64))


class POgr2Category(Base):
    __tablename__ = 'p_ogr_2_category'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(64))
    CATEGORY_ID = Column(BIGINT(20))


class POrgAddres(Base):
    __tablename__ = 'p_org_address'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_ID = Column(BIGINT(20), nullable=False)
    HOS_BRANCH = Column(String(50))
    PROVINCE = Column(String(20))
    CITY = Column(String(20))
    COUNTY = Column(String(20))
    TOWN = Column(String(100))
    ZIP_CODE = Column(String(10))
    PHONE = Column(String(20))


class POrganizationBusiClas(Base):
    __tablename__ = 'p_organization_busi_class'

    ID = Column(BIGINT(20), primary_key=True)
    BUSI_CODE = Column(String(32))
    BUSI_DESC = Column(String(64))
    ORG_CODE = Column(String(64))
    CREATE_TIME = Column(DateTime)


class POrganizationProvider(Base):
    __tablename__ = 'p_organization_provider'

    ID = Column(BIGINT(20), primary_key=True)
    CODE = Column(String(64), nullable=False, unique=True)
    NAME = Column(String(64))
    TYPE = Column(String(10), index=True)
    SUB_CATEFORY_TYPE = Column(String(10))
    CATEGORY_RULE_ID = Column(String(256))
    ADDRESS = Column(String(256))
    CONTACT_NAME = Column(String(64))
    PHONE = Column(String(20))
    CREATE_DATE = Column(DateTime)
    UPDATE_DATE = Column(DateTime)
    LEVEL_CODE = Column(String(20))
    LEVEL_NAME = Column(String(32))
    BED_CAPACITY = Column(INTEGER(11))
    OUTPATIENT_AMOUNT = Column(String(10))
    INTRODUCTION = Column(String(256))
    FLOOR_GUIDE = Column(String(1024))
    IMAGE_URL = Column(String(1024))
    EXTENDED_ATTRIBUTE = Column(String(1024))
    DISPLAY_ORDER = Column(String(128))
    STATUS = Column(INTEGER(1), nullable=False)
    ORG_SHORT_NAME = Column(String(100))
    ORG_NET_ADDRESS = Column(String(50))
    DD_COP_ID = Column(String(100))
    YLT_CODE = Column(String(50))
    YGT_CODE = Column(String(50))
    UNION_CODE = Column(String(50))
    SUPER_GOV_DEPT = Column(String(50))
    LONGITUDE = Column(DECIMAL(10, 6))
    LATITUDE = Column(DECIMAL(10, 6))
    SUPER_ORG_CODE = Column(String(50))


class POrganizationRelationship(Base):
    __tablename__ = 'p_organization_relationship'
    __table_args__ = (
        Index('index_type_etc', 'RELATIONSHIP_TYPE', 'ORGANIZATION_ID', 'PARENT_ORGANIZATION_ID', 'RULE_ID'),
    )

    RELATIONSHIP_ID = Column(BIGINT(20), primary_key=True)
    RELATIONSHIP_TYPE = Column(String(10), nullable=False)
    ORGANIZATION_ID = Column(BIGINT(20))
    PARENT_ORGANIZATION_ID = Column(BIGINT(20))
    RULE_ID = Column(String(128))
    LEAF_NODE_FLAG = Column(TINYINT(4))


class POrgdept2Gbdept(Base):
    __tablename__ = 'p_orgdept_2_gbdept'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_ID = Column(BIGINT(20), index=True)
    DEPT_ID = Column(BIGINT(20), index=True)
    GB_DEPT_ID = Column(BIGINT(20))
    ORG_CODE = Column(String(64))
    DEPT_CODE = Column(String(64))
    GB_DEPT_CODE = Column(String(64))


class RegRegister(Base):
    __tablename__ = 'reg_register'

    REGISTER_ID = Column(BIGINT(18), primary_key=True)
    HIS_REGISTER_ID = Column(String(32))
    ID_TYPE = Column(INTEGER(3))
    ID_NO = Column(String(64))
    USER_ID = Column(BIGINT(20))
    NAME = Column(String(32))
    SEX = Column(INTEGER(1))
    MOBILE_NUM = Column(String(20))
    ACCOUNT_TYPE = Column(INTEGER(3))
    ACCOUNT_NO = Column(String(30))
    PERIOD_TYPE = Column(INTEGER(3))
    TIME_POINT_ID = Column(String(128))
    TIME_POINT_DESC = Column(String(128))
    VISIT_SERIES_NUM = Column(INTEGER(3))
    WORK_SHIFT_ID = Column(String(8))
    SOURCE_NO = Column(String(8))
    REGISTER_FEE = Column(DECIMAL(12, 2))
    APPOINT_DATE_TIME = Column(DateTime)
    VISIT_DATE = Column(DateTime)
    STATUS = Column(INTEGER(1))
    REGISTER_TYPE = Column(INTEGER(3))
    INQUISITION_TYPE = Column(INTEGER(1), nullable=False)
    APP_ID = Column(String(64))
    APP_TYPE = Column(INTEGER(3))
    ORG_CODE = Column(String(32))
    ORG_NAME = Column(String(32))
    DEPT_CODE = Column(String(32))
    DEPT_NAME = Column(String(32))
    DOCTOR_CODE = Column(String(32))
    DOCTOR_NAME = Column(String(32))
    PV_START_DATE_TIME = Column(String(20))
    PV_END_DATE_TIME = Column(String(20))
    EXPIRED_DATE_TIME = Column(DateTime)
    VISIT_ID = Column(String(64))
    VISIT_STATUS = Column(INTEGER(1), server_default=text("'0'"))
    DEFRAY_ID = Column(BIGINT(20))
    DEFRAY_RESULT = Column(INTEGER(1), server_default=text("'0'"))
    DEFRAY_STATUS = Column(INTEGER(1), server_default=text("'0'"))
    SATISFY_REMARK_STATUS = Column(INTEGER(1), server_default=text("'0'"))
    SEND_STOP_REG_SMS = Column(INTEGER(1), server_default=text("'0'"))
    OPERATOR_NAME = Column(String(60))
    INPUT_DATE_TIME = Column(DateTime)
    UPDATE_DATE_TIME = Column(DateTime)
    OVER_STATUS = Column(INTEGER(1), server_default=text("'0'"))


class RemBusiScore(Base):
    __tablename__ = 'rem_busi_score'

    ID = Column(BIGINT(20), primary_key=True)
    BUSI_CODE = Column(String(16))
    SCORE_TYPE = Column(INTEGER(1))
    MSG_TEMPLATE = Column(String(512))
    PRAISE_MIN_SCORE = Column(INTEGER(11))


class RemItemDef(Base):
    __tablename__ = 'rem_item_def'

    ID = Column(BIGINT(20), primary_key=True)
    BUSI_CODE = Column(String(16))
    CONTENT = Column(String(32))
    SCORE = Column(INTEGER(11))


class RemRecord(Base):
    __tablename__ = 'rem_record'

    ID = Column(BIGINT(20), primary_key=True)
    EMPLOYEE_ID = Column(BIGINT(20), nullable=False)
    USER_ID = Column(BIGINT(20), nullable=False)
    LOGIN_ID = Column(BIGINT(20))
    USER_NAME = Column(String(32))
    BUSI_CODE = Column(String(16))
    BUSI_ORDER_ID = Column(BIGINT(20))
    SCORE_TYPE = Column(INTEGER(1))
    SCORE = Column(INTEGER(11))
    ITEM_IDS = Column(String(64))
    ITEM_DESCS = Column(String(512))
    SOURCE_TYPE = Column(INTEGER(2))
    CONTENT = Column(String(512))
    REMARK_TIME = Column(DateTime, nullable=False)
    PRAISE_FLAG = Column(INTEGER(1))


class SchdBusiTimePeriodSource(Base):
    __tablename__ = 'schd_busi_time_period_source'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(64), nullable=False)
    BUSI_CODE = Column(String(16), nullable=False)
    SOURCE_TYPE = Column(INTEGER(2), nullable=False)
    SOURCE_TYPE_VALUE = Column(String(16))
    TIME_TYPE = Column(INTEGER(11))
    START_TIME = Column(String(5), nullable=False)
    END_TIME = Column(String(5), nullable=False)
    TOTAL_NUM = Column(INTEGER(11))


class SchdBusiWorkshift(Base):
    __tablename__ = 'schd_busi_workshift'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(64))
    DEPT_CODE = Column(String(64))
    DEPT_RULE_ID = Column(String(128))
    EMPLOYEE_ID = Column(BIGINT(20))
    DOCTOR_CODE = Column(String(64))
    DOCTOR_NAME = Column(String(32))
    SCHEDULE_DATE = Column(Date)
    BUSI_SOURCE_ID = Column(BIGINT(20))
    START_TIME = Column(String(5), nullable=False)
    END_TIME = Column(String(5), nullable=False)
    SOURCE_RELEASE_FLAG = Column(INTEGER(1))
    STOP_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    TOTAL_NUM = Column(INTEGER(11))
    TIME_TOTAL_NUM = Column(INTEGER(11))
    LAST_SERIES_NUM = Column(INTEGER(11), server_default=text("'0'"))
    NOW_SERIES_NUM = Column(INTEGER(11), server_default=text("'0'"))
    BUSI_CODE = Column(String(16), nullable=False)
    YEAR = Column(String(4))
    TIME_TYPE = Column(INTEGER(11))


class SchdBusiWorkshiftSourceLocking(Base):
    __tablename__ = 'schd_busi_workshift_source_locking'

    ID = Column(BIGINT(20), primary_key=True)
    BUSI_WORKSHIFT_ID = Column(BIGINT(20), nullable=False)
    USER_ID = Column(BIGINT(20), nullable=False)
    RESERVE_EXPIRE_TIME = Column(DateTime, nullable=False)


class SchdTelWorkshift(Base):
    __tablename__ = 'schd_tel_workshift'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(64))
    DEPT_CODE = Column(String(64))
    DEPT_RULE_ID = Column(String(128))
    EMPLOYEE_ID = Column(BIGINT(20))
    DOCTOR_CODE = Column(String(64))
    DOCTOR_NAME = Column(String(32))
    SCHEDULE_DATE = Column(Date)
    START_TIME = Column(String(5), nullable=False)
    END_TIME = Column(String(5), nullable=False)
    SOURCE_RELEASE_FLAG = Column(INTEGER(1))
    RESERVE_FLAG = Column(INTEGER(1))
    RESERVE_EXPIRE_TIME = Column(DateTime)
    OCCUPY_FLAG = Column(INTEGER(1))
    YEAR = Column(String(4))


class SchdVideoWorkshift(Base):
    __tablename__ = 'schd_video_workshift'

    ID = Column(BIGINT(20), primary_key=True)
    ORG_CODE = Column(String(64))
    DEPT_CODE = Column(String(64))
    DEPT_RULE_ID = Column(String(128))
    EMPLOYEE_ID = Column(BIGINT(20))
    DOCTOR_CODE = Column(String(64))
    DOCTOR_NAME = Column(String(32))
    SCHEDULE_DATE = Column(Date)
    START_TIME = Column(String(5), nullable=False)
    END_TIME = Column(String(5), nullable=False)
    SOURCE_RELEASE_FLAG = Column(INTEGER(1))
    RESERVE_FLAG = Column(INTEGER(1))
    RESERVE_EXPIRE_TIME = Column(DateTime)
    OCCUPY_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    YEAR = Column(String(4))


class StNcdRegisterFromStatistic(Base):
    __tablename__ = 'st_ncd_register_from_statistics'

    RECORD_DATE = Column(Date, primary_key=True, nullable=False)
    ORG_CODE = Column(String(64), primary_key=True, nullable=False)
    FROM_NAME = Column(String(64))
    FROM_TYPE = Column(INTEGER(2), primary_key=True, nullable=False)
    FROM_REG_NUM = Column(INTEGER(11))


class StNcdRegisterPrePharmacyTakeStatistic(Base):
    __tablename__ = 'st_ncd_register_pre_pharmacy_take_statistics'

    RECORD_DATE = Column(Date, primary_key=True, nullable=False)
    ORG_CODE = Column(String(64), primary_key=True, nullable=False)
    PHARMACY_ID = Column(BIGINT(20), primary_key=True, nullable=False)
    PHARMACY_NAME = Column(String(64))
    PER_TAKE_NUM = Column(INTEGER(11))


class StNcdRegisterStatistic(Base):
    __tablename__ = 'st_ncd_register_statistics'

    RECORD_DATE = Column(Date, primary_key=True, nullable=False)
    ORG_CODE = Column(String(64), primary_key=True, nullable=False)
    REG_TOTAL = Column(INTEGER(11))
    PRE_TIMES = Column(INTEGER(11))
    PRE_TOTAL = Column(INTEGER(11))
    PRE_NO_CHOICE_NUM = Column(INTEGER(11))
    PRE_TAKE_NUM = Column(INTEGER(11))
    LAST_ST_TIME = Column(DateTime)


class StPrescriptionMedicinStatistic(Base):
    __tablename__ = 'st_prescription_medicin_statistics'

    RECORD_DATE = Column(Date, primary_key=True, nullable=False)
    PHARMACY_ID = Column(BIGINT(20))
    ORG_CODE = Column(String(64), primary_key=True, nullable=False)
    DEPT_CODE = Column(String(64), primary_key=True, nullable=False)
    DOCTOR_CODE = Column(String(64), primary_key=True, nullable=False)
    DEPT_NAME = Column(String(64))
    DOCTOR_NAME = Column(String(64))
    PRESCRIPTION_NUM = Column(INTEGER(11))
    VISITOR_NUM = Column(INTEGER(11))
    A_DRUGS_TOTAL = Column(DECIMAL(8, 2))
    B_DRUGS_TOTAL = Column(DECIMAL(8, 2))
    C_DRUGS_TOTAL = Column(DECIMAL(8, 2))
    N_DRUGS_TOTAL = Column(DECIMAL(8, 2))
    DRUGS_TOTAL = Column(DECIMAL(8, 2))
    CONFIRM_PRESCRIPTION_NUM = Column(INTEGER(11))
    CONFIRM_A_DRUGS_TOTAL = Column(DECIMAL(8, 2))
    CONFIRM_C_DRUGS_TOTAL = Column(DECIMAL(8, 2))
    CONFIRM_B_DRUGS_TOTAL = Column(DECIMAL(8, 2))
    CONFIRM_N_DRUGS_TOTAL = Column(DECIMAL(8, 2))
    CONFIRM_DRUGS_TOTAL = Column(DECIMAL(8, 2))


class TMockDatum(Base):
    __tablename__ = 't_mock_data'

    id = Column(BIGINT(20), primary_key=True)
    type = Column(SMALLINT(4))
    visit_id = Column(String(40))
    serial_no = Column(String(255))
    org_code = Column(String(40))
    detail = Column(Text)


class UArchieve(Base):
    __tablename__ = 'u_archieve'

    ID = Column(BIGINT(20), primary_key=True)
    USER_ID = Column(BIGINT(20), nullable=False)
    NAME_PINYIN = Column(String(32))
    ORG_CODE = Column(String(32))
    ORG_NAME = Column(String(32))
    STATUS = Column(INTEGER(1), server_default=text("'1'"))
    DATA_SOURCE_TYPE = Column(INTEGER(1), server_default=text("'1'"))
    COUNTRY = Column(String(3))
    NATION = Column(String(6))
    NATIVE_PLACE = Column(String(256))
    MARRIAGE_STATUS = Column(INTEGER(1))
    EDUCATION_LEVEL = Column(String(3))
    POLITICAL_STATUS = Column(String(3))
    JOB_TYPE = Column(String(3))
    JOB_STATUS = Column(INTEGER(1))
    PHONE_NUMBER = Column(String(20))
    CONTACT_NAME = Column(String(32))
    CONTACT_MOBILE = Column(String(20))
    HOME_ADDRESS = Column(String(256))
    DEL_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    UPLOAD_FLAG = Column(INTEGER(1), server_default=text("'0'"))
    INPUT_TIME = Column(DateTime)
    UPDATE_TIME = Column(DateTime)


class UAssociateVisitor(Base):
    __tablename__ = 'u_associate_visitor'
    __table_args__ = (
        Index('index_userId', 'LOGIN_ID', 'USER_ID'),
    )

    ID = Column(BIGINT(20), primary_key=True)
    SYS_CODE = Column(String(16))
    LOGIN_ID = Column(BIGINT(20), nullable=False)
    USER_ID = Column(BIGINT(20))
    VISIT_USER_NAME = Column(String(64))
    SEX = Column(INTEGER(1))
    MOBILE_NUMBER = Column(String(20))
    IMAGE_URL = Column(String(500))
    IMAGE_TYPE = Column(String(8))
    RELATION_TYPE = Column(INTEGER(1))
    ASSOCIATE_DESCRIBE = Column(String(512))
    CHOOSE_TIME = Column(DateTime)
    INSURANCE_CARD_NO = Column(String(100))
    PHARMACY_WXACODE = Column(LONGTEXT)
    CARD_TYPE = Column(String(64))
    IS_YELLOW_CARD = Column(String(8))
    FEE_TYPE = Column(String(64))
    PAY_ENTITY = Column(String(512))
    STATUS = Column(INTEGER(2), server_default=text("'0'"))
    UPDATE_TIME = Column(DateTime)
    ADD_TIME = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))


class UBasicInfo(Base):
    __tablename__ = 'u_basic_info'
    __table_args__ = (
        Index('Index_1', 'ID_TYPE', 'ID_NO', unique=True),
    )

    USER_ID = Column(BIGINT(20), primary_key=True)
    ID_TYPE = Column(INTEGER(3), nullable=False)
    ID_NO = Column(String(64), nullable=False)
    MOBILE_NUMBER = Column(String(20))
    LEGAL_NAME = Column(String(200))
    SEX = Column(INTEGER(1))
    BIRTHDAY = Column(DateTime)
    REGISTER_TIME = Column(DateTime)
    HOME_ADDRESS_REGION = Column(String(128))
    HOME_ADDRESS_DETAIL = Column(String(128))
    REALNAME_AUTH_FLAG = Column(INTEGER(1), nullable=False)
    ECCARD_AUTH_FLAG = Column(INTEGER(1), nullable=False)


class UDiseaseInfo(Base):
    __tablename__ = 'u_disease_info'

    ID = Column(BIGINT(20), primary_key=True)
    DISEASE_CATEGORY_ID = Column(BIGINT(20))
    DISEASE_NAME = Column(CHAR(10))
    CREATE_TIME = Column(DateTime)
    VISITOR_ID = Column(BIGINT(20))


class UHealthInfo(Base):
    __tablename__ = 'u_health_info'
    __table_args__ = (
        Index('USER_INFO_TYPE', 'USER_ID', 'INFO_TYPE', unique=True),
    )

    ID = Column(BIGINT(20), primary_key=True)
    USER_ID = Column(BIGINT(20))
    INFO_TYPE = Column(INTEGER(2), nullable=False)
    SOURCE_TYPE = Column(INTEGER(1), nullable=False)
    CONTENT = Column(String(256))
    INPUT_TIME = Column(DateTime)
    UPDATE_TIME = Column(DateTime)


class UIdentityRecongnize(Base):
    __tablename__ = 'u_identity_recongnize'
    __table_args__ = (
        Index('Index_Third_Account', 'THIRDPART_ACCOUNT', 'THIRDPART_TYPE', unique=True),
    )

    ID = Column(BIGINT(20), primary_key=True)
    THIRDPART_CODE = Column(INTEGER(2))
    THIRDPART_TYPE = Column(INTEGER(2))
    THIRDPART_ACCOUNT = Column(String(64))
    THIRDPART_META_CONTENT = Column(Text)
    THIRDPART_APP_CODE = Column(String(32))
    THIRDPART_APP_NAME = Column(String(64))
    UPDATE_TIME = Column(DateTime)


class ULoginAccount(Base):
    __tablename__ = 'u_login_account'

    ID = Column(BIGINT(20), primary_key=True)
    LOGIN_ID = Column(BIGINT(20), nullable=False, unique=True)
    TYPE = Column(INTEGER(11), nullable=False)
    LOGIN_ACCOUNT = Column(String(64), nullable=False, unique=True)
    SYS_CODE = Column(String(16))


class ULoginInfo(Base):
    __tablename__ = 'u_login_info'
    __table_args__ = (
        Index('Index_1', 'ID_TYPE', 'ID_NO', unique=True),
    )

    LOGIN_ID = Column(BIGINT(20), primary_key=True)
    ID_TYPE = Column(INTEGER(3))
    ID_NO = Column(String(64))
    MOBILE_NUMBER = Column(String(20))
    LEGAL_NAME = Column(String(200))
    PASSWORD = Column(String(200))
    GENDER = Column(String(10))
    BIRTHDAY = Column(DateTime)
    REGISTER_TIME = Column(DateTime)
    MODIFY_TIME = Column(DateTime)
    LAST_LOGIN_TIME = Column(DateTime)
    IMAGE_URL = Column(String(500))
    IMAGE_TYPE = Column(String(8))
    USER_STATUS = Column(String(10))
    HOME_ADDRESS_REGION = Column(String(128))
    HOME_ADDRESS_DETAIL = Column(String(128))
    REALNAME_AUTH_FLAG = Column(INTEGER(1), nullable=False)


class UMedicineInfo(Base):
    __tablename__ = 'u_medicine_info'

    ID = Column(BIGINT(20), primary_key=True)
    MEDI_ID = Column(BIGINT(20))
    MEDI_NAME = Column(String(64))
    MEDI_CODE = Column(String(16))
    CREATE_TIME = Column(DateTime)
    DISEASE_ID = Column(BIGINT(20))
    VISITOR_ID = Column(BIGINT(20))


class UShippingAddres(Base):
    __tablename__ = 'u_shipping_address'

    ID = Column(BIGINT(20), primary_key=True)
    USER_ID = Column(BIGINT(20), nullable=False)
    RECIPIENT_NAME = Column(String(32))
    RECIPIENT_PHONE = Column(String(32))
    PROVINCE_NAME = Column(String(32))
    CITY_NAME = Column(String(32))
    AREA_NAME = Column(String(32))
    DETAIL = Column(String(32))
    DEFAULT_FLAG = Column(INTEGER(1), server_default=text("'0'"))


class USysIrecongnize(Base):
    __tablename__ = 'u_sys_irecongnize'

    USER_ID = Column(BIGINT(20), primary_key=True, nullable=False)
    SYS_CODE = Column(String(16), primary_key=True, nullable=False)
    RECONGNIZE_ID = Column(BIGINT(20), primary_key=True, nullable=False)


class UVitalSign(Base):
    __tablename__ = 'u_vital_signs'

    ID = Column(BIGINT(20), primary_key=True)
    USER_ID = Column(BIGINT(20), index=True)
    TYPE = Column(INTEGER(2), index=True)
    VALUE = Column(String(8))
    MEASURE_TYPE = Column(INTEGER(1))
    UNIT = Column(String(8))
    MEASURE_TIME = Column(DateTime)
    MEASURE_PLACE = Column(String(32))
    INPUT_TIME = Column(DateTime)


class UWeixinFormid(Base):
    __tablename__ = 'u_weixin_formid'

    ID = Column(BIGINT(20), primary_key=True)
    APP_ID = Column(String(100))
    OPEN_ID = Column(String(100))
    FORM_ID = Column(String(200))
    CREATE_TIME = Column(DateTime)
    LOGIN_ID = Column(BIGINT(100))
