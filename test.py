import requests

url = 'http://localhost:5000/?direction=xml_to_json'
headers = {'Content-Type': 'application/xml'}
test1 = """
{
  "id": 32115,
  "user_id": 3878,
  "first_name": "Максим",
  "second_name": "Яруллин",
  "middle_name": null,
  "dict_sex_id": 1,
  "birthday": "07.08.2005",
  "citizenship_id": 185,
  "motherland": "Россия Г.Астана",
  "email": "mail@etu.ru",
  "tel_mobile": "+7 (888) 888-88-88",
  "tel_mobile_frn": "88888888888",
  "residence_country_id": 185,
  "kladr_1": "2200000000000",
  "kladr_2": "2200300000000",
  "kladr_3": "2200000100000",
  "kladr_4": "2200300002500",
  "address_txt1": "Могилевская область",
  "address_txt2": null,
  "address_txt3": null,
  "address_txt4": null,
  "street": null,
  "house": null,
  "building": null,
  "letter": null,
  "building2": null,
  "flat": null,
  "post_index": "111111",
  "has_another_living_address": false,
  "second_residence_country_id": 185,
  "second_kladr_1": null,
  "second_kladr_2": null,
  "second_kladr_3": null,
  "second_kladr_4": null,
  "second_address_txt1": null,
  "second_address_txt2": null,
  "second_address_txt3": null,
  "second_address_txt4": null,
  "second_street": null,
  "second_house": null,
  "second_building": null,
  "second_letter": null,
  "second_building2": null,
  "second_flat": null,
  "second_post_index": "111111",
  "passport_type_id": 1,
  "passport_series": "5661",
  "passport_number": "111111",
  "passport_begda": "08.9.2019",
  "passport_endda": null,
  "passport_org_code": "111-111",
  "passport_issued_by": "МВД-АВОР.ПРДЛПАРОДАЬЕК",
  "has_old_passport": true,
  "old_passport_type_id": null,
  "old_passport_series": null,
  "old_passport_number": "1111111",
  "old_passport_begda": "11.11.1111",
  "old_passport_endda": null,
  "old_passport_org_code": null,
  "old_passport_issued_by": null,
  "paid_by_another_human": null,
  "paid_passport_type_id": null,
  "paid_passport_series": null,
  "paid_passport_number": null,
  "paid_passport_begda": null,
  "paid_passport_endda": null,
  "paid_passport_org_code": null,
  "paid_passport_issued_by": null,
  "foreign_language_id": null,
  "need_hostel": null,
  "special_conditions": null,
  "is_with_disabilities": null,
  "institution_country_id": 185,
  "institution_city_id": null,
  "institution_city_text": null,
  "diploma_series": "123132",
  "diploma_number": "1211221",
  "diploma_date": "10.10.2000",
  "diploma_registration_number": "уц",
  "graduated_university_id": null,
  "has_not_found_university": null,
  "graduated_university_text": "кцу",
  "average_diploma_grade": null,
  "graduated_school_id": null,
  "has_not_found_school": null,
  "graduated_school_text": null,
  "edu_direction_id": null,
  "has_not_found_direction": null,
  "edu_direction_text": null,
  "has_no_same_level_diploma": false,
  "dict_bak_exam_reason_id": 4,
  "has_essay": true,
  "dict_asp_science_curators_id": null,
  "exam_foreign_language_id": null,
  "created_at": "2022-06-09T18:25:23.000000Z",
  "updated_at": "2023-03-05T10:12:29.000000Z",
  "created_by": 3878,
  "campaign_id": 4,
  "dict_edu_diploma_level_id": 4,
  "dict_edu_diploma_sublevel_id": 1,
  "dict_edu_diploma_name_id": 6,
  "edu_diploma_name_text": null,
  "application_scan_id": null,
  "uploaded_at": null,
  "applied_at": null,
  "revoked_at": null,
  "accepted_at": null,
  "denied_at": null,
  "dict_deny_reason_type_id": null,
  "deny_reason": null,
  "denied_by": null,
  "first_name_en": "Maxim",
  "second_name_en": "Yarullin",
  "middle_name_en": null,
  "has_no_street": true,
  "has_no_house": true,
  "has_no_second_street": false,
  "has_no_second_house": false,
  "bak_exam_wish_math": false,
  "bak_exam_wish_phys": false,
  "bak_exam_wish_rus": false,
  "bak_exam_wish_inf": false,
  "bak_exam_wish_eng": false,
  "bak_exam_wish_soc": false,
  "bak_exam_wish_chem": false,
  "has_without_exam_wish": true,
  "has_special_rights_wish": true,
  "has_priority_wish": true,
  "has_target_wish": true,
  "file_number": null,
  "is_locked": false,
  "locked_by": null,
  "applied_by": 3878,
  "revoked_by": null,
  "accepted_by": null,
  "snils": null,
  "locked_at": null,
  "revision": 1,
  "previous_application_id": null,
  "has_compatriot_wish": false,
  "is_compatriot": false,
  "has_ministry_line_wish": false,
  "is_ministry_line": false,
  "ministry_line_doc_name": null,
  "ministry_line_doc_number": null,
  "ministry_line_doc_date": null,
  "is_regrade_allowed": false,
  "idk_id": null,
  "tel_house": null,
  "is_foreigner": false,
  "is_paid": false,
  "paid_contract_num": null,
  "paid_contract_begda": null,
  "paid_contract_endda": null,
  "is_without_citizenship": false,
  "old_first_name": "Максим",
  "old_second_name": "Яруллин",
  "old_middle_name": null,
  "epgu_snils": null,
  "dict_document_return_id": 1,
  "epgu_achievement_sum": null,
  "dict_hostel_group_id": null,
  "is_first_settle_in_hostel": null,
  "dict_hostel_id": null,
  "is_send_to_sberbank": null,
  "is_sign_for_sberbank": null,
  "personal_number": null,
  "individual_number": null,
  "student_number": null,
  "mmiis_id": null,
  "is_sent_to_mmiis": false,
  "passport_name_text": null,
  "has_original_edu_diploma": false,
  "personal_data_consent_scan_id": null,
  "edu_kladr_1": "7800000000000",
  "edu_kladr_2": null,
  "edu_kladr_3": null,
  "edu_kladr_4": null,
  "edu_address_txt1": null,
  "edu_address_txt2": null,
  "edu_address_txt3": null,
  "edu_address_txt4": null,
  "is_online_bak_exam": false,
  "is_hidden_from_public_lists": false,
  "service_entrant_guid": null,
  "has_special_wish": false,
  "is_applied_offline": false,
  "photo_id": null,
  "passport_uuid": "151ad3fc-756f-46d0-8ec0-9d0355ec693a",
  "is_from_epgu": false,
  "is_applied_by_post": false,
  "is_russian_citizen_after_2022": false,
  "is_without_snils": true,
  "edu_document_uuid": "a06d0356-9997-4efe-86c0-a3348bd8b2f7",
  "is_passport_checked": false,
  "additional_files_added_at": null,
  "additional_files_checked_at": null,
  "has_additional_files": false,
  "is_additional_files_checked": false,
  "passport_epgu_id": null,
  "send_to_epgu": false,
  "is_education_document_checked": false,
  "edu_document_epgu_id": null,
  "original_edu_diploma_applied_at": null,
  "original_edu_diploma_revoked_at": null,
  "edu_document_uuid_2": "fc6ced9d-9925-4f88-aff7-279788c93829",
  "dict_mark_id": null,
  "has_epgu_original_education_document": false,
  "additional_tel_mobile": null,
  "step_navigation": 5,
  "public_code": "870-074-745 12"
}
"""

test2 = """<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" attributeFormDefault="unqualified" elementFormDefault="qualified">
	<xs:element name="EntrantChoice">
	 <xs:complexType>
		<xs:choice>
		   <xs:element type="UidType" name="Guid">
			  <xs:annotation>
				 <xs:documentation>Использовать существующий профиль поступающего. Уникальный идентификатор сгенерированный Сервисом приема</xs:documentation>
			  </xs:annotation>
		   </xs:element>
		   <xs:element name="AddEntrant">
			  <xs:annotation>
				 <xs:documentation>Создать новый профиль поступающего, т.к. нет такого</xs:documentation>
			  </xs:annotation>
			  <xs:complexType>
				 <xs:all>
					<xs:element name="Identification">
					   <xs:annotation>
						  <xs:documentation>Документ удостоверяющий личность. ФИО, указанные в нем, будут считаться ФИО поступающего. ДУЛ будет считаться подтвержденным вузом</xs:documentation>
					   </xs:annotation>
					   <xs:complexType>
						  <xs:all>
							 <xs:element type="xs:positiveInteger" name="IdDocumentType">
								<xs:annotation>
								   <xs:documentation>Тип документа. Идентификатор классификатора DocumentTypeCls</xs:documentation>
								</xs:annotation>
							 </xs:element>
							 <xs:element type="String255Type" name="DocName">
								<xs:annotation>
								   <xs:documentation>Наименование документа</xs:documentation>
								</xs:annotation>
							 </xs:element>
							 <xs:element type="String20Type" name="DocSeries" minOccurs="0">
								<xs:annotation>
								   <xs:documentation>Серия ДУЛ</xs:documentation>
								</xs:annotation>
							 </xs:element>
							 <xs:element type="String50Type" name="DocNumber">
								<xs:annotation>
								   <xs:documentation>Номер ДУЛ</xs:documentation>
								</xs:annotation>
							 </xs:element>
							 <xs:element type="xs:date" name="IssueDate">
								<xs:annotation>
								   <xs:documentation>Дата выдачи. Шаблон "2006-01-02"</xs:documentation>
								</xs:annotation>
							 </xs:element>
							 <xs:element type="String500Type" name="DocOrganization">
								<xs:annotation>
								   <xs:documentation>Огранизация, выдавшая документ</xs:documentation>
								</xs:annotation>
							 </xs:element>
							 <xs:element name="Fields" minOccurs="0">
								<xs:annotation>
								   <xs:documentation>Реквизиты, в зависимости от типа документа</xs:documentation>
								</xs:annotation>
								<xs:complexType>
								   <xs:sequence>
									  <xs:any maxOccurs="unbounded" namespace="##any" processContents="skip" />
								   </xs:sequence>
								</xs:complexType>
							 </xs:element>
						  </xs:all>
					   </xs:complexType>
					</xs:element>
					<xs:element type="SnilsType" name="Snils" minOccurs="0">
					   <xs:annotation>
						  <xs:documentation>СНИЛС - обязательный для граждан РФ</xs:documentation>
					   </xs:annotation>
					</xs:element>
					<xs:element type="xs:positiveInteger" name="IdGender">
					   <xs:annotation>
						  <xs:documentation>Идентификатор классификатора GenderCls</xs:documentation>
					   </xs:annotation>
					</xs:element>
					<xs:element type="xs:date" name="Birthday">
					   <xs:annotation>
						  <xs:documentation>Дата рождения. Шаблон "2006-01-02"</xs:documentation>
					   </xs:annotation>
					</xs:element>
					<xs:element type="String500Type" name="Birthplace">
					   <xs:annotation>
						  <xs:documentation>Место рождения</xs:documentation>
					   </xs:annotation>
					</xs:element>
					<xs:element type="String120Type" name="Phone" minOccurs="0">
					   <xs:annotation>
						  <xs:documentation>Телефон</xs:documentation>
					   </xs:annotation>
					</xs:element>
					<xs:element type="String150Type" name="Email" minOccurs="0">
					   <xs:annotation>
						  <xs:documentation>Электронный адрес</xs:documentation>
					   </xs:annotation>
					</xs:element>
					<xs:element type="xs:positiveInteger" name="IdOksm">
					   <xs:annotation>
						  <xs:documentation>Гражданство - Идентификатор классификатора OksmCls</xs:documentation>
					   </xs:annotation>
					</xs:element>
					<xs:element name="FreeEducationReason" minOccurs="0">
					   <xs:complexType>
						  <xs:all>
							 <xs:element type="xs:positiveInteger" name="IdFreeEducationReason">
								<xs:annotation>
								   <xs:documentation>Основания для получения бесплатного образования (для иностранца). Идентификатор классификатора FreeEducationReasonCls</xs:documentation>
								</xs:annotation>
							 </xs:element>
							 <xs:element type="xs:positiveInteger" name="IdOksmFreeEducationReason" minOccurs="0">
								<xs:annotation>
								   <xs:documentation>Идентификатор классификатора OkcmCls. Если IdFreeEducationReason = "Международный договор", то передается страна, с которой заключен договор</xs:documentation>
								</xs:annotation>
							 </xs:element>
						  </xs:all>
					   </xs:complexType>
					</xs:element>
					<xs:element name="AddressList">
					   <xs:annotation>
						  <xs:documentation>Список адресов абирутиента</xs:documentation>
					   </xs:annotation>
					   <xs:complexType>
						  <xs:sequence>
							 <xs:element name="Address" maxOccurs="unbounded">
								<xs:annotation>
								   <xs:documentation>Адрес</xs:documentation>
								</xs:annotation>
								<xs:complexType>
								   <xs:all>
									  <xs:element type="xs:boolean" name="IsRegistration">
										 <xs:annotation>
											<xs:documentation>Является ли данный адрес регистрацией поступающего</xs:documentation>
										 </xs:annotation>
									  </xs:element>
									  <xs:element type="String1024Type" name="FullAddr">
										 <xs:annotation>
											<xs:documentation>Полный адрес</xs:documentation>
										 </xs:annotation>
									  </xs:element>
									  <xs:element type="xs:positiveInteger" name="IdRegion">
										 <xs:annotation>
											<xs:documentation>Идентификатор классификатора RegionCls</xs:documentation>
										 </xs:annotation>
									  </xs:element>
									  <xs:element type="String255Type" name="City">
										 <xs:annotation>
											<xs:documentation>Населенный пункт</xs:documentation>
										 </xs:annotation>
									  </xs:element>
								   </xs:all>
								</xs:complexType>
							 </xs:element>
						  </xs:sequence>
					   </xs:complexType>
					</xs:element>
				 </xs:all>
			  </xs:complexType>
		   </xs:element>
		</xs:choice>
	 </xs:complexType>
	</xs:element>
   <xs:simpleType name="String9Type">
      <xs:restriction base="xs:string">
         <xs:maxLength value="9" />
         <xs:minLength value="1" />
      </xs:restriction>
   </xs:simpleType>
   <xs:simpleType name="String13Type">
      <xs:restriction base="xs:string">
         <xs:maxLength value="13" />
         <xs:minLength value="1" />
      </xs:restriction>
   </xs:simpleType>
   <xs:simpleType name="SnilsType">
      <xs:annotation>
         <xs:documentation>СНИЛС</xs:documentation>
      </xs:annotation>
      <xs:restriction base="xs:string">
         <xs:length value="11" />
         <xs:pattern value="\d{11}" />
      </xs:restriction>
   </xs:simpleType>
   <xs:simpleType name="UidType">
      <xs:restriction base="xs:string">
         <xs:maxLength value="36" />
         <xs:minLength value="10" />
      </xs:restriction>
   </xs:simpleType>
   <xs:simpleType name="String20Type">
      <xs:restriction base="xs:string">
         <xs:maxLength value="20" />
         <xs:minLength value="1" />
      </xs:restriction>
   </xs:simpleType>
   <xs:simpleType name="String50Type">
      <xs:restriction base="xs:string">
         <xs:maxLength value="50" />
         <xs:minLength value="1" />
      </xs:restriction>
   </xs:simpleType>
   <xs:simpleType name="String120Type">
      <xs:restriction base="xs:string">
         <xs:maxLength value="120" />
         <xs:minLength value="1" />
      </xs:restriction>
   </xs:simpleType>
   <xs:simpleType name="String150Type">
      <xs:restriction base="xs:string">
         <xs:maxLength value="150" />
         <xs:minLength value="1" />
      </xs:restriction>
   </xs:simpleType>
   <xs:simpleType name="String255Type">
      <xs:restriction base="xs:string">
         <xs:maxLength value="255" />
         <xs:minLength value="1" />
      </xs:restriction>
   </xs:simpleType>
   <xs:simpleType name="String500Type">
      <xs:restriction base="xs:string">
         <xs:maxLength value="500" />
         <xs:minLength value="1" />
      </xs:restriction>
   </xs:simpleType>
   <xs:simpleType name="String1024Type">
      <xs:restriction base="xs:string">
         <xs:maxLength value="1024" />
         <xs:minLength value="1" />
      </xs:restriction>
   </xs:simpleType>
</xs:schema>"""

# response = requests.post(url, headers=headers, data=test1.encode('utf-8'))
response = requests.post(url, headers=headers, data=test2.encode('utf-8'))

print(response.text)
