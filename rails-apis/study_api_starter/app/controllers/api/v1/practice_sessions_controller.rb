module Api
  module V1
    class PracticeSessionsController < ApplicationController
      # TODO: implement index, show, create, update, and destroy.
      # Compare the request method and path with config/routes.rb.
      def index
        render json: []
      end

      def show
        render json: { todo: "find by ID or return 404" }, status: :not_implemented
      end

      def create
        render json: { todo: "permit fields, save, return 201 or 422" }, status: :not_implemented
      end

      def update
        render json: { todo: "find, permit fields, update" }, status: :not_implemented
      end

      def destroy
        render json: { todo: "find, delete, return 204" }, status: :not_implemented
      end
    end
  end
end
