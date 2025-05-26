{
  "_type": "Project",
  "name": "Hospital Admission Sequence",
  "ownedElements": [
    {
      "_type": "UMLModel",
      "name": "Model",
      "ownedElements": [
        {
          "_type": "UMLSequenceDiagram",
          "name": "Admission Sequence Diagram",
          "ownedElements": [
            {
              "_type": "UMLActor",
              "name": "Patient"
            },
            {
              "_type": "UMLClassifierRole",
              "name": "Receptionist"
            },
            {
              "_type": "UMLClassifierRole",
              "name": "Hospital System"
            },
            {
              "_type": "UMLClassifierRole",
              "name": "Database"
            },
            {
              "_type": "UMLMessage",
              "name": "درخواست پذیرش",
              "source": "Patient",
              "target": "Receptionist"
            },
            {
              "_type": "UMLMessage",
              "name": "درخواست اطلاعات",
              "source": "Receptionist",
              "target": "Patient"
            }
            // ادامه پیام‌ها به همین شکل اضافه می‌شود
          ]
        }
      ]
    }
  ]
}