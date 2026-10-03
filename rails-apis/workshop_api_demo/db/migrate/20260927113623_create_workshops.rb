class CreateWorkshops < ActiveRecord::Migration[8.1]
  def change
    create_table :workshops do |t|
      t.string :title
      t.integer :capacity
      t.date :starts_on

      t.timestamps
    end
  end
end
