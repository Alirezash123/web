@startuml
actor Patient
participant Receptionist
participant "Hospital System" as System
participant Database

Patient -> Receptionist: درخواست پذیرش
Receptionist -> Patient: درخواست اطلاعات (شناسه، بیمه و ...)
Patient -> Receptionist: ارائه اطلاعات
Receptionist -> System: ثبت اطلاعات بیمار
System -> Database: بررسی سوابق بیمار
Database --> System: تأیید اطلاعات/سوابق
System --> Receptionist: تأیید ثبت
Receptionist -> System: درخواست تخصیص تخت/نوبت
System -> Database: بررسی تخت‌های موجود
Database --> System: اطلاعات تخت
System --> Receptionist: تأیید تخصیص تخت/نوبت
Receptionist -> Patient: ارجاع به بخش/پزشک

@enduml