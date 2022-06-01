from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models

app = FastAPI()

class Item(BaseModel):
	id: int
	name: str
	description: str 
	price: int 
	on_offer: bool 

	class Config:
		# Automatically serialize sql alchemy objects into JSON
		orm_mode=True


db = SessionLocal()

@app.get('/items', response_model=List[Item], status_code=status.HTTP_200_OK)
def get_all_items():
	items = db.query(models.Item).all()

	return items

@app.get('/item/{item_id}',response_model=Item, status_code=status.HTTP_200_OK)
def get_an_item(item_id: int):
	item = db.query(models.Item).filter(models.Item.id == item_id).first()
	if not item:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No item with that ID")
	
	return item 

@app.post('/items', response_model=Item, status_code=status.HTTP_201_CREATED)
def create_an_item(item:Item):
	db_item=db.query(models.Item).filter(models.Item.name==item.name).first()
	if db_item:
		raise HTTPException(status_code=400, detail="Item already exists.")

	new_item = models.Item(
		name=item.name,
		price=item.price,
		description=item.description,
		on_offer=item.on_offer
		)


	db.add(new_item)
	db.commit()

	return new_item

@app.put('/item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
def update_an_item(item_id: int, item:Item):
	item_to_update= db.query(models.Item).filter(models.Item.id == item_id).first()
	if not item_to_update:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No item with that ID")

	item_to_update.name = item.name
	item_to_update.price = item.price 
	item_to_update.description = item.description
	item_to_update.on_offer = item.on_offer

	db.commit()
	return item_to_update


@app.delete('/item/{item_id}')
def delete_item(item_id: int):
	item_to_delete = db.query(models.Item).filter(models.Item.id == item_id).first()
	if not item_to_delete:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No item with that ID")

	db.delete(item_to_delete)
	db.commit()

	return item_to_delete

